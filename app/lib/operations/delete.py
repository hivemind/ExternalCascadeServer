
import requests

r = requests.delete("http://127.0.0.1:5000/options/1", )

print(r.status_code, r.text)