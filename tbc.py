import argparse
import datetime
import requests
import json

from urllib.parse import urlparse, parse_qs, urlencode

def basic_request(url, data, headers, save_fpath):
    result = requests.post(url, data=data, headers=headers)  
    print(result.status_code)
    print(result.cookies)
    with open(save_fpath, "w") as file:
        file.write(result.text)

def construct_body(template, chart_calendar_value, currencies, filter_combo):
    print(template)
    test_qdict = parse_qs(template)
    
    print(test_qdict)
    
    test_qdict['chartCalendarValue'] = chart_calendar_value
    test_qdict['useCalendar'] = 'true'
    test_qdict['currencyCodes'] = currencies
    test_qdict['filterCombo'] = filter_combo
    
    print(test_qdict)
    
    test_qs = urlencode(test_qdict)
    
    print(test_qs)
    
    return test_qs    

if __name__ == '__main__':
    print("TBC Test")
    
    test_url = "https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=filterChart&p_p_cacheability=cacheLevelPage"
    
    test_body = "currencyCodes=USD%3Atrue%2CEUR%3Atrue%2CGBP%3Atrue&filterCombo=3&chartCalendarValue=4%2F1%2F2023&useCalendar=true"
    
    test_data = construct_body(
        template=test_body,
        chart_calendar_value=datetime.datetime(year=2023, month=6, day=1).strftime('%m/%d/%Y'),
        currencies="USD:true,EUR:false,GBP:false",
        filter_combo='3',
    )
    
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
    
    basic_request(
        url=test_url,
        data=test_data,
        headers=headers,
        save_fpath='./results/tbc_test_01.html'
    )
    
    # TODO: parse
    # var chartData = "[{date:'May 29, 2023',USD:2.5876},{date:'May 30, 2023',USD:2.5823},{date:'May 31, 2023',USD:2.5919},{date:'Jun 1, 2023',USD:2.5972},{date:'Jun 2, 2023',USD:2.6396},{date:'Jun 3, 2023',USD:2.6335},{date:'Jun 4, 2023',USD:2.6335}]";