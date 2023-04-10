import requests

# Set up API endpoint and headers
url = "https://api.openai.com/v1/analyze_data"
headers = {
    "Content-Type": "text/csv",
    "Authorization": f"Bearer {API_KEY}"
}

# Open and read the CSV file
with open('example.csv', 'rb') as file:
    csv_content = file.read()

# Send the file to the OpenAI API
response = requests.post(url, headers=headers, data=csv_content)

# Process the response
if response.status_code == 200:
    # Success! Process the response here
    print(response.json())
else:
    # Error handling here
    print(f"Error {response.status_code}: {response.text}")
