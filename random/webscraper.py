import requests
from bs4 import BeautifulSoup

class Results:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def getTitle(self):
        return self.title
    
    def getLink(self):
        return self.link


def getResults():
    response = requests.get('http://thejournal.ie')
    soup = BeautifulSoup(response.text, "html.parser")
    h4 = soup.find_all("h4")
    
    myResults = [Results(h_tag.a.string,h_tag.a.get('href')) for h_tag in h4]

    print("<<<")
    # for h in h4:
    #     print(h.a.string + "\t" + h.a.get('href'))

    for a in myResults:
        print(a.getTitle() + "\t" + a.getLink())

    print(">>>")

if __name__ == "__main__":
    getResults()