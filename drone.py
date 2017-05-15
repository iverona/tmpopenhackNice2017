import requests

url = "http://droneapi.ddns.net:1235/vehicle/8ce02f05"

headers = {
    'cache-control': "no-cache",
    'postman-token': "4d64b78e-e386-0d7b-0959-5e089e498505"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)