import requests

endpoint = "http://localhost:8080/api/products/3/delete/"

get_response = requests.delete(endpoint, params={"abc": 123}, json={"title": "123"})
print(get_response.status_code)