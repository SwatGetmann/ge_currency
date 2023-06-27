import argparse
import datetime
import requests
import json
import re
import pathlib

from math import ceil
from urllib.parse import urlencode

from exceptions import *
from validations import *

from tbc_tests import *

def basic_request(url, data, headers, session=None):
    if session:
        result = requests.post(url, data=data, headers=headers)
    else:
        result = session.post(url, data=data, headers=headers)
    print(result.status_code)
    print(result.cookies)
    return result


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


def crawl(save_fpath, start_dt, currencies=['USD'], session=None):
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
    
    if session:
        session.headers = headers

    res = basic_request(
        url=url,
        data=body,
        headers=headers,
        session=session,
    )
    save_content(path=save_fpath, content=res.text)
    return res


def parse(content, currencies=['USD'], debug=False):
    match = re.search('\n\s+var chartData = \"(.*)\";', content)
    validate_match(match)
    
    if debug:
        print(match)
        print(match.group(1))
    
    chart_data_text = match.group(1)
    chart_data_text, _ = re.subn('date:', '"date":', chart_data_text)
    
    if debug:
        print(chart_data_text)
    
    for currency in currencies:        
        chart_data_text, _ = re.subn(
            '{}:'.format(currency), 
            '"{}":'.format(currency),
            chart_data_text
        )
        if debug:
            print(chart_data_text)

    currency_values = eval(chart_data_text)
    
    if debug:
        print(currency_values)
        print(currency_values[0])
        print(len(currency_values))
    
    return currency_values


def save_content(path, content):
    print("Saving: {}...".format(path))
    with open(path, "w") as file:
        file.write(content)


def read_content(path):
    content = None
    print("Reading: {}...".format(path))
    with open(path, "r") as file:
        content = file.read()
    print(len(content))
    return content


def marker_content(save_fpath_prefix, pages, first_day_today):
    return json.dumps({
        'save_fpath_prefix': save_fpath_prefix,
        'pages': pages,
        'first_day_today': first_day_today,
    })


OFFSET_DAYS = 7
OFFSET_DAYS_FROM_TODAY = 10


def paginated_crawl(save_fpath_prefix, marker_fpath, start_dt, end_dt, currencies=['USD']):    
    if currencies is None or not currencies:
        raise NotProvidedParameter(parameter_name='currencies')
    
    if not start_dt:
        raise NotProvidedParameter(parameter_name='Start DT || chartCalendarValue')
    
    if not end_dt:
        raise NotProvidedParameter(parameter_name='End DT')
    
    print("Paginated crawl for {} - {}".format(end_dt, start_dt))
    
    # precalulcate how many requests are necessary
    # we know that TBC gives the desired date in the middle of response list
    # so [-3, -2, -1, 0 = cur date, +1, +2, +3]
    # based on that, we can go back only for 3 days witihn one request
    
    first_day_today = False
    
    if start_dt.date() == datetime.date.today():
        # first page gives last 7 days already (OFFSET_DAYS)
        # next ones should be done with -3 offset
        first_day_today = True

    delta_days = ceil((start_dt - end_dt) / datetime.timedelta(days=1))
    
    if first_day_today:
        pages = 1 + int((delta_days - OFFSET_DAYS_FROM_TODAY) // OFFSET_DAYS)
    else:
        pages = int(delta_days // OFFSET_DAYS)
    
    print("Delta Days : {} /// Pages to go back: {}".format(delta_days, pages))
    
    if not pathlib.Path(marker_fpath).exists():
        pathlib.Path(marker_fpath).parents[0].mkdir(parents=True, exist_ok=True)
    
    save_content(
        path=marker_fpath,
        content=marker_content(save_fpath_prefix, pages, first_day_today)
    )
    
    print("Marker is written to {}".format(marker_fpath))
    
    session = requests.Session()
    
    t_day_delta = 0
    for i in range(0, pages+1):
        t_day_delta = OFFSET_DAYS * i
        if first_day_today:
            t_day_delta += (i > 0) * (OFFSET_DAYS_FROM_TODAY - OFFSET_DAYS + 1)
            
        t_start_dt = start_dt - datetime.timedelta(days=t_day_delta)
        
        print(t_start_dt)
        
        crawl(
            save_fpath=paginated_crawl_save_fpath(save_fpath_prefix, i), 
            start_dt=t_start_dt,
            currencies=currencies,
            session=session,
        ) 


def paginated_crawl_save_fpath(prefix, index):
    return "{}_p{:03}.html".format(prefix, index)

def paginated_parse(save_fpath_prefix, marker_fpath, start_dt, end_dt, currencies=['USD']):
    # read marker
    # get context: `save_fpath_prefix`, `pages`, `first_day_today`
    
    if not pathlib.Path(marker_fpath).exists():
        raise PaginatedParseMarkerNotFound(marker_fpath=marker_fpath)
    
    marker = json.loads(read_content(marker_fpath))
    
    # add validations for marker!
    
    results = []
    
    for pi in range(0, marker['pages']):
        content = read_content(
            paginated_crawl_save_fpath(save_fpath_prefix, pi)
        )
        validate_content(content)
        currency_values = parse(content, currencies=currencies)
        
        # print(currency_values)
        
        # concatenate all in list / DF s !
        results.append(currency_values)
    
    results = [item for sublist in results for item in sublist]
    results.sort(key=lambda x: x['date'])
    return results


if __name__ == '__main__':
    print("TBC Test")

    # test_6()
    test_7()    