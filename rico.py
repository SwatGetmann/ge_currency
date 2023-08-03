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
    print(len(result.text))
    print(result.cookies)
    return result 

def crawl(save_fpath_prefix, currencies=['USD'], session=None):
    # We're scraping conversion rates from the seed page
    url = "https://www.rico.ge/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    }
            
    page = basic_request(
        url=url,
        headers=headers,
    )
                
    save_content(
        path=save_fpath_generator('html', save_fpath_prefix),
        content=page.content,
        bytes=True
    )
        
    # == TODO: Parse conversion rates & save as ... ? parquet? into SQLite?
    
    # df = pd.DataFrame(result.json())
    # parquet_path = save_fpath_generator('parquet', save_fpath_prefix)
    # save_parquet(path=parquet_path, df=df)


def save_fpath_generator(ftype=None, prefix=None):
    if not ftype:
        raise NotProvidedParameter(parameter_name='ftype')
    
    if ftype == 'json':
        return "./results/{}.json".format(prefix)
    elif ftype == 'parquet':
        return "./parquets/{}.parquet".format(prefix)
    elif ftype == 'html':
        return "./results/{}.html".format(prefix)
    else:
        raise UnsupportedValueParameter(parameter_name='ftype')


parser = argparse.ArgumentParser(
    description="""
    Currency API reader fot rico.ge.
        (one of the most popular microfinancing companies in Georgia).
    NOTE: Crawling data is provided ONLY for the current day.
    """
)
parser.add_argument('--currencies', 
                    choices=['USD', 'EUR', 'GBP'],
                    default='USD',
                    nargs='+',
                    required=True,
                    help='currency to select'
)
parser.add_argument('--save_prefix',
                    default='RICO_currency_read',
                    help='file prefix to store data and markers with'
)


if __name__ == '__main__':
    args = parser.parse_args()
    print(args)
    
    crawl(
        save_fpath_prefix=args.save_prefix, 
        currencies=args.currencies, 
        session=None
    )
