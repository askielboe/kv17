import requests

api_url = 'http://api.statbank.dk/v1/'

api_method = 'subjects'

payload = {
    "lang": "en",
    "format": "JSON",
    "subjects": [
        "02",
        "2401"
    ],
    "includeTables": True,
    "recursive": True
}

r = requests.post(api_url + api_method, data=payload)

print(r.json())
