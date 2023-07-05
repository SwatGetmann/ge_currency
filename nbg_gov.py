import argparse
import datetime
import requests
import json
import pandas as pd

from urllib.parse import urlparse, parse_qs, urlencode

from util import *
from exceptions import *
from validations import *

def basic_request(url, headers):
    result = requests.get(url, headers=headers)  
    print(result.status_code)
    print(result.json())
    print(result.cookies)
    return result 

def construct_url(template_url, start, end, currencies):
    test_url_parsed = urlparse(template_url)
    print(test_url_parsed)
    
    test_qdict = parse_qs(test_url_parsed.query)
    
    print(test_qdict)
    
    test_qdict['start'] = start
    test_qdict['end'] = end
    test_qdict['currencies'] = currencies
    
    print(test_qdict)
    
    test_qs = urlencode(test_qdict)
    
    print(test_qs)
    
    print(test_url_parsed._replace(query=test_qs))
    print(test_url_parsed._replace(query=test_qs).geturl())

    return test_url_parsed._replace(query=test_qs).geturl()


def crawl(save_fpath_prefix, start_dt, end_dt, currencies=['USD'], session=None):
    url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&currencies=USD&end=2023-06-13T04%3A37%3A39.818Z&start=2023-05-24T04%3A37%3A39.818Z"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://nbg.gov.ge/en/monetary-policy/currency',
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
    
    for currency in currencies:
        curr_test_url = construct_url(
            template_url=url,
            start=start_dt,
            end=end_dt,
            currencies=currency
        )
        
        result = basic_request(
            url=curr_test_url,
            headers=headers,
        )
                
        save_content(
            path=save_fpath_generator('json', save_fpath_prefix, currency),
            content=json.dumps(result.json())
        )
        
        df = pd.DataFrame(result)
        parquet_path = save_fpath_generator('parquet', save_fpath_prefix, currency)
        save_parquet(path=parquet_path, df=df)


def save_fpath_generator(ftype=None, prefix=None, currency=None):
    if not ftype:
        raise NotProvidedParameter(parameter_name='ftype')
    
    if ftype == 'json':
        return "./results/{}_{}.json".format(prefix, currency)
    elif ftype == 'parquet':
        return "./parquets/{}_{}.parquet".format(prefix, currency)
    else:
        raise UnsupportedValueParameter(parameter_name='ftype')


parser = argparse.ArgumentParser(
    description='Currency API reader fot NBG (National Bank of Georgia).'
)
parser.add_argument('--start_dt', 
                    type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d"),
                    default=datetime.datetime.now(),
                    help='a start date for curerncy to be read'
)
parser.add_argument('--end_dt', 
                    type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d"),  
                    default=datetime.datetime.now(),
                    help='an end date for curerncy to be read'
)
parser.add_argument('--currencies', 
                    choices=['USD', 'EUR', 'GBP'],
                    default='USD',
                    nargs='+',
                    required=True,
                    help='currency to select'
)
parser.add_argument('--save_prefix',
                    default='NBG_currency_read',
                    help='file prefix to store data and markers with'
)


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    
    crawl(
        save_fpath_prefix=args.save_prefix, 
        start_dt=args.start_dt.strftime('%F'),
        end_dt=args.end_dt.strftime('%F'),
        currencies=args.currencies, 
        session=None
    )
    