# Georgian Currency Client

## About

An app, that daily tracks currencies in Georgia, starting with Lari(GEL) and US Dollar (USD).

## Plans

* [+] Read TBC bank API
* [+] Paginate APIs
    * [+, Necessary only for TBC] paginated crawling, session-safe
    * [+] paginated parsing
* [+] Support for EUR, USD, GBP
    * [+] TBC
    * [+] nbg.gov.ge
* [+] Parquets save for API results
* [+] CLI for Crawling & Parsing APIs
* [+-] Unit Tests
    * should be rewritten account to test methodologies
* [+] Add Jupyter Notebooks for test/example purposes
* Compare TBC & National Bank (NBG) rates
    * Acquire the data for the last year (2023)
    * Compare daily deltas
    * Plot results out
* Cache results
    * Reuse already scraped data
* Store the data in local sqlite if required
* Read Other Currency Rate APIs 
    * Liberty Bank
    * BOG