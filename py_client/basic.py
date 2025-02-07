import requests

endpoint = "http://localhost:8080/api/"

get_response = requests.post(endpoint, params={"abc": 123}, json={"title": "123"})
# in this case, the data will be in json and will be accessible in the data variable in response...

# get_response = requests.get(endpoint, data={"query": "Hello World"})
# in this case, the data will be in form data and will be accessible in the form variable in response...

print(get_response.text)
print(get_response.status_code)

#  HTTP request -> HTML
#  Rest Api HTTP Request -> JSON