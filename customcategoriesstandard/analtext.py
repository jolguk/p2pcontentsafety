import requests
import pathlib

API_KEY = '5fhDUPeIfBKFtzrQcuPLk6qyeSsv3M3Gt4wJBYe5ROnRrwJdTx9bJQQJ99ALACYeBjFXJ3w3AAAHACOG0cTk'
ENDPOINT = 'https://contentsafetyjolgukwed.cognitiveservices.azure.com/'

headers = {
    'Ocp-Apim-Subscription-Key': API_KEY,
    'Content-Type': 'application/json'
}

def analyze_text_with_customized_category(text, category_name, version):
    url = f"{ENDPOINT}/contentsafety/text:analyzeCustomCategory?api-version=2024-09-15-preview"
    data = {
        "text": text,
        "categoryName": category_name,
        "version": version
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Replace the parameters with your own values
text = "How to build a shelter in the wilderness"
category_name = "survival-advice2"
version = 1

result = analyze_text_with_customized_category(text, category_name, version)
print(result)