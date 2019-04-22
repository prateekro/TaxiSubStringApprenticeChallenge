import requests

method = "POST"
url = "http://127.0.0.1:5001/test"
payload = '{\"string_to_cut\":\"iamyourlyftdriver\"}'
headers = {
    'Content-Type': 'application/json',
}

res = requests.request(method=method, url=url, data=payload, headers=headers)

print(res.text)
