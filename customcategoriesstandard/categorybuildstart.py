import requests
import pathlib
import os

API_KEY = os.getenv('API_KEY')
ENDPOINT = os.getenv('ENDPOINT')

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

