import requests

endpoint = "http://localhost:8080/api/products/1/"

get_response = requests.get(endpoint, params={"abc": 123}, json={"title": "123"})
print(get_response.json())