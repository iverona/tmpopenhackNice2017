import requests
import json

url = "https://eu11.salesforce.com/services/apexrest/openAPI/troubleTicket"
auth_token = "00D0Y000001i7TL!AR0AQETNMX5oDqnHbk3MyA.QqhexEd0nqjS8dnys5ShnxAOLRCe5EYaqwHe58aritRYuLLjMcF1A86J75VnRa8FfkZFMJdzY"



headers = {
    'x-prettyprint': "1",
    'content-type': "application/json",
    'authorization': "Bearer %s" % auth_token, 
    'cache-control': "no-cache",
    'postman-token': "e27b78ef-ee64-76ed-8470-76b261bade52"
    }

def create_sf_ticket(handle, text, lat, lon):
	jPayload = {
		 "subStatus": "Pending",
		  "status": "Submitted",		  
		  "twitterHandle": "%s" % handle,
		  "subject": "%s" % text,
		  "location_long": "%s" % lon,
		  "location_lat": "%s" % lat,		
		  "asset": "02i0Y0000003nWtQAI",  
		}

	response = requests.post(url, data=json.dumps(jPayload), headers=headers)

# Example
# create_sf_ticket("iveronar", "test report from twitter!", "1.23", "3.21")
