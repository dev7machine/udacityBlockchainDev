import requests
import json

blockHash = "364f7bb9e3e062ac27781bd0e6dcbabd0757ebc4a027ceb179470c5fdb5ee472"
mUrl = f"http://localhost:8000/block/hash/{blockHash}"
response = requests.get(mUrl)
print(response.status_code)
print(json.dumps(response.json(), indent=4))