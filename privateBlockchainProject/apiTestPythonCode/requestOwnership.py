import requests
import json


json_data = {
    'address': '1F3sAm6ZtwLAUnj7d38pGFxtP3RVEvtsbV',
}

response = requests.post('http://localhost:8000/requestValidation', json=json_data)
print(response.status_code)
print(json.dumps(response.json(), indent=4))

