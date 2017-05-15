import requests
import json

url = "https://eu11.salesforce.com/services/apexrest/openAPI/troubleTicket"
auth_token = "00D0Y000001i7TL!AR0AQETNMX5oDqnHbk3MyA.QqhexEd0nqjS8dnys5ShnxAOLRCe5EYaqwHe58aritRYuLLjMcF1A86J75VnRa8FfkZFMJdzY"

jPayload = {
		 "subStatus": "Pending",
		  "status": "Submitted",
		  # "targetResolutionDate": "2017-05-31T10:19:00.000Z",
		  # "creationDate": "2017-05-11T13:05:09.000Z",
		  # "type": "Question",
		  # "severity": "Medium",
		  "description": "Description string Postman Test2",
		  # "statusChangeDate": "2017-05-11T10:19:00.000Z",
		  # "correlationId": "123",
		  # "statusChangeReason": "Reason string",
		  # "resolutionDate": "2017-05-14T13:05:09.000Z",
		  "twitterHandle": "@thomas",
		  "subject": "Subject from Python with Location",
		  "location_long": "45.02",
		  "location_lat": "15",		
		  "asset": "02i0Y0000003nWtQAI",  
		}

headers = {
    'x-prettyprint': "1",
    'content-type': "application/json",
    'authorization': "Bearer %s" % auth_token, 
    'cache-control': "no-cache",
    'postman-token': "e27b78ef-ee64-76ed-8470-76b261bade52"
    }

def create_sf_ticket(handle, text, lat, long):
	response = requests.post(url, data=json.dumps(jPayload), headers=headers)

create_sf_ticket("iveronar", "test report from twitter!", "1.23", "3.21")