import requests

endpoint = "http://localhost:8080/api/products/1/update/"

data = {
    "title": "World",
    "price": 123.23
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())