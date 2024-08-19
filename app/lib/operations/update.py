import json
import requests

data = {
    "field_id": "customfield_10900",
    "value": "value 2",
    "parent_id": "0",
    "enabled": True
}

r = requests.put("http://127.0.0.1:5000/options/1", data=json.dumps(data), headers={'Content-Type': 'application/json'})

print(r.status_code, r.text)