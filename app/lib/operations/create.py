import json
import random

import requests

def create(id):
    data = {
        "id": str(id),
        "field_id": "customfield_10100",
        "value": f"Value {id}",
        "parentId": random.randint(0, id),
        "enabled": True
    }
    return requests.post("http://127.0.0.1:5002/options", data=json.dumps(data), headers={'Content-Type': 'application/json'})

counter = 0

while counter < 500:
    create(counter)
    counter += 1

