import requests

response = requests.get('http://thejournal.ie')

print(response.content)
print("<<<<")
print(response.text)
