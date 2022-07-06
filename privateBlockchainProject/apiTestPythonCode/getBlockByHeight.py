import requests
import json

response = requests.get('http://localhost:8000/block/height/0')
print(response.status_code)
print(json.dumps(response.json(), indent=4))