import requests
import json

from urllib.parse import urlparse, parse_qs, urlencode

def basic_request(url, headers, save_fpath):
    result = requests.get(url, headers=headers)  
    print(result.status_code)
    print(result.json())
    print(result.cookies)
    with open(save_fpath, "w") as file:
        file.write(json.dumps(result.json()[0]))

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

if __name__ == '__main__':
    print("Test")
    
    test_url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&currencies=USD&end=2023-06-13T04%3A37%3A39.818Z&start=2023-05-24T04%3A37%3A39.818Z"
    
    test_url_v2 = construct_url(
        template_url=test_url,
        start='2023-05-01',
        end='2023-05-31',
        currencies='USD'
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
    
    basic_request(
        url=test_url_v2,
        headers=headers,
        save_fpath='./results/test_01.json'
    )
    
    test_url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&currencies=USD&end=2023-06-13T04%3A37%3A39.818Z&start=2023-05-24T04%3A37%3A39.818Z"
    
    basic_request(
        url=test_url,
        headers=headers,
        save_fpath='./results/test_02.json'
    )