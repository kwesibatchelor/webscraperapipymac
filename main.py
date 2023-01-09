import requests

response = requests.get("http://www.cnn.com")

#print(response.status_code)
#print(response.text)
print(response.json)
