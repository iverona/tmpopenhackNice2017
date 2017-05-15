import requests
import json

url = "https://eu11.salesforce.com/services/apexrest/openAPI/customer"

headers = {
    'x-prettyprint': "1",
    'authorization': "Bearer 00D0Y000001i7TL!AR0AQETNMX5oDqnHbk3MyA.QqhexEd0nqjS8dnys5ShnxAOLRCe5EYaqwHe58aritRYuLLjMcF1A86J75VnRa8FfkZFMJdzY",
    'cache-control': "no-cache",
    'postman-token': "bb3f31f4-a976-2700-a742-3325b7d22ba0"
    }

response = requests.request("GET", url, headers=headers)

# print(response.text)

# print response.status_code
jRep = json.loads(response.text)
for i in jRep:
	print i