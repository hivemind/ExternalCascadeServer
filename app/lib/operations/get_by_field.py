import requests

r = requests.get("http://127.0.0.1:5000/options/field/customfield_10900")

print(r.json())