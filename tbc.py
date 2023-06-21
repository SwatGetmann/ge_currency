import argparse
import datetime
import requests
import json
import re

import pathlib
from math import ceil

from urllib.parse import urlparse, parse_qs, urlencode

def basic_request(url, data, headers, save_fpath):
    result = requests.post(url, data=data, headers=headers)  
    print(result.status_code)
    print(result.cookies)
    with open(save_fpath, "w") as file:
        file.write(result.text)
    return result

def validate_request(request):
    if request.status_code != 200:
        raise InvalidResponseCode(request.status_code)

def validate_content(content):
    if content == '':
        raise EmptyContent()

def validate_match(match):
    if match is None:
        raise MatchNotFound()

class InvalidResponseCode(BaseException):
    def __init__(self, code, message="Response Code is not successful (200)") -> None:
        self.code = code
        self.message = message
        super().__init__(self.message)
    
class EmptyContent(BaseException):
    def __init__(self, message="Content is empty") -> None:
        self.message = message
        super().__init__(self.message)

class MatchNotFound(BaseException):
    def __init__(self, message="Match for Response Content had not been found") -> None:
        self.message = message
        super().__init__(self.message)

class NotProvidedParameter(BaseException):
    def __init__(self, parameter_name='ParameterName', message=" is not provided!") -> None:
        self.parameter_name = parameter_name
        self.message = self.parameter_name + message
        super().__init__(self.message)


def currency_codes_body_str(currencies):
    map = {
        'USD': False,
        'EUR': False,
        'GBP': False,
    }
    keys = map.keys()
    
    for currency in currencies:
        if currency in keys:
            map[currency] = True
    
    return ",".join(["{}:{}".format(i[0], str.lower(str(i[1]))) for i in map.items()])    


def crawl(save_fpath, start_dt, currencies=['USD']):
    url = "https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=filterChart&p_p_cacheability=cacheLevelPage"
    
    if currencies is None or not currencies:
        raise NotProvidedParameter(parameter_name='currencies')
    
    if not start_dt:
        raise NotProvidedParameter(parameter_name='Start DT || chartCalendarValue')
    
    body_dict = {
        'currencyCodes': currency_codes_body_str(currencies),
        'filterCombo': str(3), # don't know but let's hard code for now
        'chartCalendarValue': start_dt.strftime('%m/%d/%Y'),
        'useCalendar': str.lower(str(True)),
    }
    
    body = urlencode(body_dict)
        
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.tbcbank.ge",
        "DNT": "1",
        "Referer": "https://www.tbcbank.ge/web/en/exchange-rates",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "TE": "trailers"
    }
    
    res = basic_request(
        url=url,
        data=body,
        headers=headers,
        save_fpath=save_fpath,
    )
    
    return res


def parse(content, currencies=['USD']):
    match = re.search('\n\s+var chartData = \"(.*)\";', content)
    validate_match(match)
    
    print(match)
    print(match.group(1))
    
    chart_data_text = match.group(1)
    chart_data_text, _ = re.subn('date:', '"date":', chart_data_text)
    print(chart_data_text)
    
    for currency in currencies:        
        chart_data_text, _ = re.subn(
            '{}:'.format(currency), 
            '"{}":'.format(currency),
            chart_data_text
        )
        print(chart_data_text)

    currency_values = eval(chart_data_text)
    print(currency_values)
    print(currency_values[0])
    print(len(currency_values))
    
    return currency_values


def read_saved_result(read_fpath):
    read_fpath = './results/tbc_test_01.html'
    content = None
    with open(read_fpath, "r") as file:
        content = file.read()
    
    print(len(content))
    return content


def paginated_crawl(save_fpath_prefix, marker_fpath, start_dt, end_dt, currencies=['USD']):    
    if currencies is None or not currencies:
        raise NotProvidedParameter(parameter_name='currencies')
    
    if not start_dt:
        raise NotProvidedParameter(parameter_name='Start DT || chartCalendarValue')
    
    if not end_dt:
        raise NotProvidedParameter(parameter_name='End DT')
    
    # precalulcate how many requests are necessary
    # we know that TBC gives the desired date in the middle of response list
    # so [-3, -2, -1, 0 = cur date, +1, +2, +3]
    # based on that, we can go back only for 3 days witihn one request
    
    delta_days = ceil((start_dt - end_dt) / datetime.timedelta(days=1))
    pages = int(delta_days // 3)
    
    print("Delta Days : {} /// Pages to go back: {}".format(delta_days, pages))
    
    if not pathlib.Path(marker_fpath).exists():
        pathlib.Path(marker_fpath).parents[0].mkdir(parents=True, exist_ok=True)
    
    with open(marker_fpath, 'w') as f:
        f.write(
            json.dumps({
                'save_fpath_prefix': save_fpath_prefix,
                'pages': pages
            })
        )
    
    print("Marker is written to {}".format(marker_fpath))
    
    for i in range(0, pages+1):
        crawl(
            save_fpath="{}_p{:03}.html".format(save_fpath_prefix, i), 
            start_dt=start_dt - datetime.timedelta(days=3*i),
            currencies=currencies
        ) 


# def paginated_parse():
#     # TBD


if __name__ == '__main__':
    print("TBC Test")
    
    # TEST 1 - Old Date, Single Currency
    # res = crawl(
    #     save_fpath='./results/tbc_test_04A.html',
    #     start_dt=datetime.datetime(year=2022, month=7, day=1)
    # )
    # validate_request(res)
    # validate_content(res.text)
    # currency_values = parse(res.text)
    
    # # TEST 2 - Old Date, 2 Currencies
    # # des = desired
    # des_currencies = ['USD', 'EUR']                                             
    # res = crawl(
    #     save_fpath='./results/tbc_test_04B.html', 
    #     start_dt=datetime.datetime(year=2022, month=12, day=11),
    #     currencies=des_currencies
    # )
    # validate_request(res)
    # validate_content(res.text)
    # currency_values = parse(res.text, currencies=des_currencies)
    
    # # TEST 3 - Parse from Read
    # # Read Previously collected file to parse
    # content = read_saved_result('./results/tbc_test_01.html')
    # validate_content(content)
    # des_currencies = ['USD']
    # currency_values = parse(content)
    
    # TEST 4 - FAIL STATE - Generates a NotProvidedParameter exception
    # Destined to fail
    # des = desired
    # des_currencies = []                                             
    # res = crawl(
    #     save_fpath='./results/tbc_test_04B.html', 
    #     start_dt=datetime.datetime(year=2023, month=5, day=1),
    #     currencies=des_currencies
    # )
    # validate_request(res)
    # validate_content(res.text)
    # currency_values = parse(res.text, currencies=des_currencies)
    
    # TEST 5 - Paginated crawl - Last 1 Week
    # start_dt = datetime.datetime.now()
    # end_dt = start_dt - datetime.timedelta(days=7)
    
    # paginated_crawl(
    #     save_fpath_prefix='./results/TBC_TEST5_LastWeek', 
    #     marker_fpath='./markers/TBC_TEST5_LastWeek.marker', 
    #     start_dt=start_dt,
    #     end_dt=end_dt, 
    #     currencies=['USD']
    # )
    
    # TEST ^ - Paginated crawl - Arbitrary Dates
    start_dt = datetime.datetime(year=2023, month=5, day=1)
    end_dt = start_dt - datetime.timedelta(days=30)
    
    paginated_crawl(
        save_fpath_prefix='./results/TBC_TEST5_LastWeek', 
        marker_fpath='./markers/TBC_TEST5_LastWeek.marker', 
        start_dt=start_dt,
        end_dt=end_dt, 
        currencies=['USD']
    )
    