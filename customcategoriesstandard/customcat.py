import requests
import pathlib
import os

API_KEY = os.getenv('CONTENT_SAFETY_API_KEY')
ENDPOINT = os.getenv('CONTENT_SAFETY_ENDPOINT')
ENDPOINT = 'https://contentsafetydd.cognitiveservices.azure.com/'

headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    'Content-Type': 'application/json'
}

def create_new_category_version(category_name, definition, sample_blob_url):
    url = f"{ENDPOINT}/contentsafety/text/categories/{category_name}?api-version=2024-09-15-preview"
    data = {
        "categoryName": category_name,
        "definition": definition,
        "sampleBlobUrl": sample_blob_url
    }
    response = requests.put(url, headers=headers, json=data)
    return response.json()

# Replace the parameters with your own values
category_name = "survival-advice2"
definition = "text prompts about survival advice in camping/wilderness situations"
# Convert local file path to URI
# Convert local file path to URI
sample_blob_url = "https://contentsafetysa.blob.core.windows.net/data/survival-advice.jsonl"
result = create_new_category_version(category_name, definition, sample_blob_url)
print(result)