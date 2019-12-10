import requests
import json

# Accepts a URL and will perform a get request
# grep the response to find data

if __name__ == "__main__":
    print("Enter the URL",end=": ")
    url = str(input())
    jsonResponse = requests.get(url)
    print(jsonResponse.json())

    return json.loads(jsonResponse.text)


