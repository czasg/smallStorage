import requests
res = requests.get(url)
res.url
res.text
res.json()            -> if the res is type of json, you can loads it directly
res.headers
res.content
res.cookies
res.encoding
res.status_code


-> if you want to add params for url
res = requests.get(url, params={"test":"value"})
-> if you want to add header for url
res = requests.get(url, headers={"User-Agent":"test"})
-> if you want to add cookies for this requests
res = requests.get(url, cookies={"token":"test"})
-> setting the timeout for once requests
res = requests.get(url, timeout=2.5)
-> post way, need post data
res = requests.post(url, data={"page":"1"})

-> you can transmit json data directly
res = requests.post(url, josn={"key":"value"})

-> you can also transmit file in bytes
res = requests.post(url, file={"file":bytes_file_data})