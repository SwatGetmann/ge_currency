import datetime

from validations import *
from tbc import *

def test_1():
    # TEST 1 - Old Date, Single Currency
    res = crawl(
        save_fpath='./results/tbc_test_04A.html',
        start_dt=datetime.datetime(year=2022, month=7, day=1)
    )
    validate_request(res)
    validate_content(res.text)
    currency_values = parse(res.text)

def test_2():
    # TEST 2 - Old Date, 2 Currencies
    # des = desired
    des_currencies = ['USD', 'EUR']                                             
    res = crawl(
        save_fpath='./results/tbc_test_04B.html', 
        start_dt=datetime.datetime(year=2022, month=12, day=11),
        currencies=des_currencies
    )
    validate_request(res)
    validate_content(res.text)
    currency_values = parse(res.text, currencies=des_currencies)
    
def test_3():
    # TEST 3 - Parse from Read
    # Read Previously collected file to parse
    content = read_saved_result('./results/tbc_test_01.html')
    validate_content(content)
    des_currencies = ['USD']
    currency_values = parse(content)
    
def test_3b():
    # TEST 3 - Parse from Read - Multiple Currencies - FAILS now
    # Read Previously collected file to parse
    content = read_saved_result('./results/tbc_test_01.html')
    validate_content(content)
    des_currencies = ['USD', 'EUR']
    currency_values = parse(content, currencies=des_currencies)
    
def test_4():
    # TEST 4 - FAIL STATE - Generates a NotProvidedParameter exception
    # Destined to fail
    # des = desired
    des_currencies = []                                             
    res = crawl(
        save_fpath='./results/tbc_test_04B.html', 
        start_dt=datetime.datetime(year=2023, month=5, day=1),
        currencies=des_currencies
    )
    validate_request(res)
    validate_content(res.text)
    currency_values = parse(res.text, currencies=des_currencies)

def test_5():
    # TEST 5 - Paginated crawl - Last 1 Week
    end_dt = datetime.datetime.now()
    start_dt = end_dt - datetime.timedelta(days=25)
    
    paginated_crawl(
        save_fpath_prefix='./results/TBC_TEST5_LastWeek', 
        marker_fpath='./markers/TBC_TEST5_LastWeek.marker', 
        start_dt=start_dt,
        end_dt=end_dt, 
        currencies=['USD']
    )

def test_6():
    # TEST 6 - Paginated crawl - Arbitrary Dates
    end_dt = datetime.datetime(year=2023, month=5, day=1)
    start_dt = end_dt - datetime.timedelta(days=30)
    
    paginated_crawl(
        save_fpath_prefix='./results/TBC_TEST5_Month', 
        marker_fpath='./markers/TBC_TEST5_Month.marker', 
        start_dt=start_dt,
        end_dt=end_dt, 
        currencies=['USD']
    )
    
def test_7():
    # TEST 7 - Paginated parse - Arbitrary Dates
    end_dt = datetime.datetime(year=2023, month=5, day=1)
    start_dt = end_dt - datetime.timedelta(days=30)
    
    results = paginated_parse(
        save_fpath_prefix='./results/TBC_TEST5_Month', 
        marker_fpath='./markers/TBC_TEST5_Month.marker', 
        start_dt=start_dt,
        end_dt=end_dt, 
        currencies=['USD']
    )
    print(results)
    

def test_8(name="3Months"):
    # TEST 8 - 3 Months Scope - Crawl
    end_dt = datetime.datetime(year=2023, month=1, day=1)
    start_dt = end_dt - datetime.timedelta(days=90)
    
    paginated_crawl(
        save_fpath_prefix='./results/TBC_TEST5_{}'.format(name), 
        marker_fpath='./markers/TBC_TEST5_{}.marker'.format(name), 
        start_dt=start_dt,
        end_dt=end_dt, 
        currencies=['USD']
    )
    
def test_9(name="3Months"):
    # TEST 8 - 3 Months Scope - Crawl
    end_dt = datetime.datetime(year=2023, month=1, day=1)
    start_dt = end_dt - datetime.timedelta(days=90)
    
    results = paginated_parse(
        save_fpath_prefix='./results/TBC_TEST5_{}'.format(name),
        marker_fpath='./markers/TBC_TEST5_{}.marker'.format(name),
        start_dt=start_dt,
        end_dt=end_dt, 
        currencies=['USD']
    )
    print(results)