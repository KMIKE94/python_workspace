import requests
from bs4 import BeautifulSoup

response = requests.get('http://thejournal.ie')
soup = BeautifulSoup(response.text, "html.parser")
h4 = soup.find_all("h4")
my_soup = BeautifulSoup("<html></html>")
html = my_soup.html

print("<<<")
for h in h4:
    print(h.a.string + "\t" + h.a.get('href'))
    h2 = my_soup.new_tag("h2")
    h2.string = h.a.string
    a = my_soup.new_tag("a", href=h.a.get('href'))
print(">>>")