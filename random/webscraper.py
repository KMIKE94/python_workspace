import requests
from bs4 import BeautifulSoup

response = requests.get('http://thejournal.ie')
soup = BeautifulSoup(response.text, "html.parser")
h4 = soup.find_all("h4")

print("<<<")
for h in h4:
    print(h.a.string + "\t" + h.a.get('href'))
print(">>>")