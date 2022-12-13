import requests

trigger_url = 'http://localhost:8080'

url = trigger_url + '/items/'

payload = {
"name": "Derrick",
"description": "A Software Developer",
"price": 100.00,
"tax": 10.00
}

response =requests.post(url, json=payload)
print(response.json())
