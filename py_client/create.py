import requests

endpoint = "http://localhost:8080/api/products/"

get_response = requests.post(endpoint, json={"title": "123"})

print(get_response.json())