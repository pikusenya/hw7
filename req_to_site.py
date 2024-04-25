import requests

response = requests.post("http://127.0.0.1:5000/calculation", json={"a": 5, "b": 10, "action": "+_"})
print()