import requests

endpoint = "http://localhost:8080/api/products/"

get_response = requests.get(endpoint)

print(get_response.json())