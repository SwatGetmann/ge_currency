import argparse
import datetime
import requests
import json

from urllib.parse import urlparse, parse_qs, urlencode

def basic_request(url, headers):
    result = requests.get(url, headers=headers)  
    print(result.status_code)
    print(result.json())
    print(result.cookies)
    return result 


def save_content(path, content):
    with open(path, "w") as file:
        file.write(content)


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
    
    print("Test")
    
    test_url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&currencies=USD&end=2023-06-13T04%3A37%3A39.818Z&start=2023-05-24T04%3A37%3A39.818Z"
    
    curr_test_url = construct_url(
        template_url=test_url,
        start=args.start_dt.strftime('%F'),
        end=args.end_dt.strftime('%F'),
        currencies=args.currencies
    )
    
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
    
    result = basic_request(
        url=curr_test_url,
        headers=headers,
    )
    
    save_path = './results/{}.json'.format(args.save_prefix)
    
    save_content(
        path=save_path,
        content=json.dumps(result.json())
    )