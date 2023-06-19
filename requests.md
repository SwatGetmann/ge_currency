```
curl "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&end=2023-02-28T19^%^3A59^%^3A59.999Z&start=2022-12-31T20^%^3A00^%^3A00.000Z" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: en" -H "Accept-Encoding: gzip, deflate, br" -H "DNT: 1" -H "Connection: keep-alive" -H "Referer: https://nbg.gov.ge/en/monetary-policy/currency" -H "Cookie: _ga_MBKC1SW239=GS1.1.1665070577.3.1.1665071341.0.0.0; _ga=GA1.3.978586715.1659780461; acceptedCookie=false; TS0147d5cf=01d86c96a5f0a01e038218246eeb15733db60a1126e68cfdb67c31f2672d8842c0152a6da184708f95ccdb9aa7ec9f2b0709fe2e63ad80769c41eb41806ed9994f7b9c82ff; next-i18next=en" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache"
```

# 1
```
curl "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&date=2023-06-13" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: en" -H "Accept-Encoding: gzip, deflate, br" -H "DNT: 1" -H "Connection: keep-alive" -H "Referer: https://nbg.gov.ge/en/monetary-policy/currency" -H "Cookie: _ga_MBKC1SW239=GS1.1.1665070577.3.1.1665071341.0.0.0; _ga=GA1.3.978586715.1659780461; acceptedCookie=false; TS0147d5cf=01d86c96a5f2995d43cd209d4905967341a8d2ced5b598388010ceaabe9c32e20cd5d37a68e6c68996c2d0ed3a2b5584cf63ef0cdee7e8b7a149505a552c8d1e85b8d81046; next-i18next=en" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache"
```

# 2
```
curl "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&currencies=USD&end=2023-06-13T04^%^3A37^%^3A39.818Z&start=2023-05-24T04^%^3A37^%^3A39.818Z" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0" -H "Accept: application/json, text/plain, */*" -H "Accept-Language: en" -H "Accept-Encoding: gzip, deflate, br" -H "DNT: 1" -H "Connection: keep-alive" -H "Referer: https://nbg.gov.ge/en/monetary-policy/currency" -H "Cookie: _ga_MBKC1SW239=GS1.1.1665070577.3.1.1665071341.0.0.0; _ga=GA1.3.978586715.1659780461; acceptedCookie=false; TS0147d5cf=01d86c96a5f2995d43cd209d4905967341a8d2ced5b598388010ceaabe9c32e20cd5d37a68e6c68996c2d0ed3a2b5584cf63ef0cdee7e8b7a149505a552c8d1e85b8d81046; next-i18next=en" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache"
```

## var
```
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.Cookies.Add((New-Object System.Net.Cookie("_ga_MBKC1SW239", "GS1.1.1665070577.3.1.1665071341.0.0.0", "/", "nbg.gov.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("_ga", "GA1.3.978586715.1659780461", "/", "nbg.gov.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("acceptedCookie", "false", "/", "nbg.gov.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("TS0147d5cf", "01d86c96a5f2995d43cd209d4905967341a8d2ced5b598388010ceaabe9c32e20cd5d37a68e6c68996c2d0ed3a2b5584cf63ef0cdee7e8b7a149505a552c8d1e85b8d81046", "/", "nbg.gov.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("next-i18next", "en", "/", "nbg.gov.ge")))
Invoke-WebRequest -UseBasicParsing -Uri "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/?currencies=USD&currencies=USD&end=2023-06-13T04%3A37%3A39.818Z&start=2023-05-24T04%3A37%3A39.818Z" `
-WebSession $session `
-UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0" `
-Headers @{
"Accept" = "application/json, text/plain, */*"
  "Accept-Language" = "en"
  "Accept-Encoding" = "gzip, deflate, br"
  "Referer" = "https://nbg.gov.ge/en/monetary-policy/currency"
  "DNT" = "1"
  "Sec-Fetch-Dest" = "empty"
  "Sec-Fetch-Mode" = "no-cors"
  "Sec-Fetch-Site" = "same-origin"
  "Sec-GPC" = "1"
  "Pragma" = "no-cache"
  "Cache-Control" = "no-cache"
}
```


# TBC Requests

## Posix Windows CURL
```
curl 'https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=filterChart&p_p_cacheability=cacheLevelPage' -X POST -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.tbcbank.ge' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://www.tbcbank.ge/web/en/exchange-rates' -H 'Cookie: JSESSIONID=PUAWZqMWuoq2q3ICpiF6MhBQ; TS01987dc4=01863392edc20fb0183a36fe7e153ef41e2990d2da54ce831f58d73fa1f3000b23b0c0a1d9ea2717bb9d24b5350d3328cbc8e6e643; cc_cookie={"level": ["necessary","analytics","preferences", "targeting"]}; TS01441710=01863392ed9759d4b5c07869566c5174aca9021a4a0d8fdf55ef158029bd549bca2856b7add966d0f221dd96133a2575d5a7764f4e' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-GPC: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers' --data-raw 'currencyCodes=USD%3Atrue%2CEUR%3Atrue%2CGBP%3Atrue&filterCombo=1&chartCalendarValue=&useCalendar=false'
```
## PowerShell CURL
```
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.Cookies.Add((New-Object System.Net.Cookie("JSESSIONID", "PUAWZqMWuoq2q3ICpiF6MhBQ", "/", "www.tbcbank.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("TS01987dc4", "01863392edc20fb0183a36fe7e153ef41e2990d2da54ce831f58d73fa1f3000b23b0c0a1d9ea2717bb9d24b5350d3328cbc8e6e643", "/", "www.tbcbank.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("cc_cookie", "{`"level`": [`"necessary`",`"analytics`",`"preferences`", `"targeting`"]}", "/", "www.tbcbank.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("TS01441710", "01863392ed9759d4b5c07869566c5174aca9021a4a0d8fdf55ef158029bd549bca2856b7add966d0f221dd96133a2575d5a7764f4e", "/", "www.tbcbank.ge")))
Invoke-WebRequest -UseBasicParsing -Uri "https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=filterChart&p_p_cacheability=cacheLevelPage" `
-Method POST `
-WebSession $session `
-UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0" `
-Headers @{
"Accept" = "*/*"
  "Accept-Language" = "en-US,en;q=0.5"
  "Accept-Encoding" = "gzip, deflate, br"
  "X-Requested-With" = "XMLHttpRequest"
  "Origin" = "https://www.tbcbank.ge"
  "DNT" = "1"
  "Referer" = "https://www.tbcbank.ge/web/en/exchange-rates"
  "Sec-Fetch-Dest" = "empty"
  "Sec-Fetch-Mode" = "cors"
  "Sec-Fetch-Site" = "same-origin"
  "Sec-GPC" = "1"
  "Pragma" = "no-cache"
  "Cache-Control" = "no-cache"
  "TE" = "trailers"
} `
-ContentType "application/x-www-form-urlencoded; charset=UTF-8" `
-Body "currencyCodes=USD%3Atrue%2CEUR%3Atrue%2CGBP%3Atrue&filterCombo=1&chartCalendarValue=&useCalendar=false"
```

## POSIX - 2
```
curl 'https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=filterChart&p_p_cacheability=cacheLevelPage' -X POST -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://www.tbcbank.ge' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://www.tbcbank.ge/web/en/exchange-rates' -H 'Cookie: JSESSIONID=PUAWZqMWuoq2q3ICpiF6MhBQ; TS01987dc4=01863392edc20fb0183a36fe7e153ef41e2990d2da54ce831f58d73fa1f3000b23b0c0a1d9ea2717bb9d24b5350d3328cbc8e6e643; cc_cookie={"level": ["necessary","analytics","preferences", "targeting"]}; TS01441710=01863392edb28355618613d614f5468da4686c59b22cdf481959b8476b006c6270868c40e9665c08d11cba89e834200bafbb030123' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-GPC: 1' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'TE: trailers' --data-raw 'currencyCodes=USD%3Atrue%2CEUR%3Atrue%2CGBP%3Atrue&filterCombo=3&chartCalendarValue=4%2F1%2F2023&useCalendar=true'
```

### Power Shell - 2
```
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.Cookies.Add((New-Object System.Net.Cookie("JSESSIONID", "PUAWZqMWuoq2q3ICpiF6MhBQ", "/", "www.tbcbank.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("TS01987dc4", "01863392edc20fb0183a36fe7e153ef41e2990d2da54ce831f58d73fa1f3000b23b0c0a1d9ea2717bb9d24b5350d3328cbc8e6e643", "/", "www.tbcbank.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("cc_cookie", "{`"level`": [`"necessary`",`"analytics`",`"preferences`", `"targeting`"]}", "/", "www.tbcbank.ge")))
$session.Cookies.Add((New-Object System.Net.Cookie("TS01441710", "01863392edb28355618613d614f5468da4686c59b22cdf481959b8476b006c6270868c40e9665c08d11cba89e834200bafbb030123", "/", "www.tbcbank.ge")))
Invoke-WebRequest -UseBasicParsing -Uri "https://www.tbcbank.ge/web/en/web/guest/exchange-rates?p_p_id=exchangerates_WAR_tbcpwexchangeratesportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_resource_id=filterChart&p_p_cacheability=cacheLevelPage" `
-Method POST `
-WebSession $session `
-UserAgent "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0" `
-Headers @{
"Accept" = "*/*"
  "Accept-Language" = "en-US,en;q=0.5"
  "Accept-Encoding" = "gzip, deflate, br"
  "X-Requested-With" = "XMLHttpRequest"
  "Origin" = "https://www.tbcbank.ge"
  "DNT" = "1"
  "Referer" = "https://www.tbcbank.ge/web/en/exchange-rates"
  "Sec-Fetch-Dest" = "empty"
  "Sec-Fetch-Mode" = "cors"
  "Sec-Fetch-Site" = "same-origin"
  "Sec-GPC" = "1"
  "Pragma" = "no-cache"
  "Cache-Control" = "no-cache"
  "TE" = "trailers"
} `
-ContentType "application/x-www-form-urlencoded; charset=UTF-8" `
-Body "currencyCodes=USD%3Atrue%2CEUR%3Atrue%2CGBP%3Atrue&filterCombo=3&chartCalendarValue=4%2F1%2F2023&useCalendar=true"
```
