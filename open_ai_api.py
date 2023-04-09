import requests

url = "https://api.openai.com/v1/endpoint"
headers = {"Authorization": "Bearer <your_api_key>"}

response = requests.get(url, headers=headers)

