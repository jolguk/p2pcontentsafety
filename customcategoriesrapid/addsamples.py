import requests

API_KEY = '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk'
ENDPOINT = 'https://contentsafetyjolgukwed.cognitiveservices.azure.com/'


import requests
import json

url = "https://contentsafetyjolgukwed.cognitiveservices.azure.com//contentsafety/text/incidents/problem1:addIncidentSamples?api-version=2024-02-15-preview"

payload = json.dumps({
  "IncidentSamples": [
    {
      "text": "They have stopped charging"
    },
    {
      "text": "I can't pair them with my phone"
    },
    {
      "text": "The battery life is too short"
    },
    {
      "text": "The sound quality is poor"
    }
  ]
})
headers = {
  'Ocp-Apim-Subscription-Key': '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)