import requests
import json


walletAddr = "1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV"
mUrl = f"http://localhost:8000/blocks/{walletAddr}"
response = requests.get(mUrl)
print(response.status_code)
print(json.dumps(response.json(), indent=4))