

API_KEY = '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk'
ENDPOINT = 'https://contentsafetyjolgukwed.cognitiveservices.azure.com/'


import requests

url = f"{ENDPOINT}contentsafety/text/incidents?api-version=2024-02-15-preview"

payload = {}
headers = {
  'Ocp-Apim-Subscription-Key': API_KEY
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)