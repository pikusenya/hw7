import requests

# response = requests.post("http://127.0.0.1:5000/calculation", json={"a": 5, "b": 10, "action": "-"})
# response = requests.post("http://127.0.0.1:5000/text_editor", json={"text": "qwerty", "action": "alter"})
response = requests.post("http://127.0.0.1:5000/parser", json={"text": "Contact me at 89991112233 or jane.smith@gmail.com for any questions.", "action": "email"})
# response = requests.get("http://127.0.0.1:5000/")
print(response.text)
