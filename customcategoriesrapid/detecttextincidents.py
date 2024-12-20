# Description: This script is used to deploy incident samples to the Content Moderator service.

API_KEY = '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk'
ENDPOINT = 'https://contentsafetyjolgukwed.cognitiveservices.azure.com/'


import requests
import json

url = "https://contentsafetyjolgukwed.cognitiveservices.azure.com/contentsafety/text:detectIncidents?api-version=2024-02-15-preview"

payload = json.dumps({
  "text": "sound quality is poor",
  "incidentNames": [
    "problem1"
  ]
})
headers = {
  'Ocp-Apim-Subscription-Key': '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)