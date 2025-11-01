import os
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ceecgokul2024.atlassian.net/rest/api/3/project"

# Load credentials from environment variables
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("MY_TOKEN")

auth = HTTPBasicAuth(email, api_token)

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers, auth=auth)

output = json.loads(response.text)

for i in range(0,len(output)):
    print(output[i]["name"])
