# LyftApprenticeChallenge  [![Awesome](https://github.com/prateekro/ref/blob/master/badge/awesomebadge.svg)](https://github.com/prateekro/)

###### API Module for Lyft Apprentice - Sample Code [Code Language: Python]

---
#### Steps to be followed in sequence to run:
> Install flask dependencies `pip install flask`
>
> Start Project `py lyftSample.py`
>

The application should start on ` http://127.0.0.1` at port `5001` or goto ` http://127.0.0.1:5001/`

---
#### Steps to initiate test
> Route at `/test` 
> 
> Request method `POST` 
> 
> headers `'Content-Type': "application/json"`
>
> body `{"string_to_cut": "iamyourlyftdriver"}`

---
#### Snippet of Code logic
```
for enum, i in enumerate(list(data['string_to_cut'])):
    if enum%3 == 2:
        output += i
return '%s' % output
```

---
#### Unit Test

- A code snippet from file `lyftSample.py`

```
with app.test_client() as lyftCase:
    resp = lyftCase.post('/test', json={
        'string_to_cut': 'iamyourlyftdriver'
    })
    if resp.data.decode('utf-8') == '{"return_string":"muydv"}\n':
        print('Test Success:', resp.data.decode('utf-8'))
``` 

- A test file `testSample.py` to run sample test case

```
import requests

method = "POST"
url = "http://127.0.0.1:5001/test"
payload = '{\"string_to_cut\":\"iamyourlyftdriver\"}'
headers = {
    'Content-Type': 'application/json',
}

res = requests.request(method=method, url=url, data=payload, headers=headers)

print(res.text)
```
