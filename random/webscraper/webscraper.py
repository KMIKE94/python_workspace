import requests
import json
from bs4 import BeautifulSoup
from marshmallow import Schema, fields

class Results:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def getTitle(self):
        return self.title
    
    def getLink(self):
        return self.link

class NewsSchema(Schema):
    article = fields.Str()
    link = fields.Str()

def getResults(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    main_container = soup.find("div", {"class": "mainContainer content"})

    headers = main_container.findAll("h4")
    myResults = [Results(h_tag.a.string,h_tag.a.get('href')) for h_tag in headers]

    object_schema = NewsSchema()

    jsonResponse = object_schema.dumps(myResults, many=True)

    return jsonResponse

def createDictionary(results):
    dictionary = {}
    for result in results:
        dictionary.update({result.getTitle():result.getLink()})

    return dictionary