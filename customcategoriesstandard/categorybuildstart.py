import requests
import pathlib

API_KEY = '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk'
ENDPOINT = 'https://contentsafetyjolgukwed.cognitiveservices.azure.com/'

headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    'Content-Type': 'application/json'
}

def trigger_category_build_process(category_name, version):
    url = f"https://contentsafetyjolgukwed.cognitiveservices.azure.com//contentsafety/text/categories/survival-advice2:build?api-version=2024-09-15-preview&version=1"
    response = requests.post(url, headers=headers)
    return response.status_code
    return response.json()

# Replace the parameters with your own values
category_name = "survival-advice"
version = 1

result = trigger_category_build_process(category_name, version)
print(result)

