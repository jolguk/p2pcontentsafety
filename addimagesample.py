import requests

API_KEY = '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk'
ENDPOINT = 'https://contentsafetyjolgukwed.cognitiveservices.azure.com/'

headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    'Content-Type': 'application/json'
}

import json

url = ENDPOINT + "contentsafety/image/incidents/imageproblem2:addIncidentSamples?api-version=2024-02-15-preview"

payload = json.dumps({
  "IncidentSamples": [
    {
      "image": {
                "bloburl": "https://contentsafetysa.blob.core.windows.net/data/OIP.jpg"
      }
    }
  ]
})
headers = {
  'Ocp-Apim-Subscription-Key': API_KEY,
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
