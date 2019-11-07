import requests
import json

if __name__ == "__main__":
    print("Enter the URL",end=": ")
    url = str(input())
    jsonResponse = requests.get(url)
    print(jsonResponse.json())

    customer = json.loads(jsonResponse.text)
    print(customer["firstName"])


