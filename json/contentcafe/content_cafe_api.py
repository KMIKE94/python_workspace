from typing import List
import requests
import xml.etree.cElementTree as elementTree
from model.model import Review, Summary, AuthorNote, Excerpt, CoverImageInfo, ImageType

BASE_URI = "https://contentcafe2.btol.com/contentcafe/contentcafe.asmx/Single"
BASE_JACKET_URI = "https://contentcafe2.btol.com/ContentCafe/Jacket.aspx"

CONTENTTYPE_REVIEW = "ReviewDetail"
CONTENTTYPE_ANNOTATION = "AnnotationDetail"
CONTENTTYPE_AUTHORNOTES = "BiographyDetail"
CONTENTTYPE_EXCERPT = "ExcerptDetail"
CONTENTTYPE_SMALLCOVER = "S"
CONTENTTYPE_MEDIUMCOVER = "M"
CONTENTTYPE_LARGECOVER = "L"

PROVIDER_URI = "http://contentcafe2.btol.com/"


# Need to refactor - Spent too much time understanding the XML traversal
# Would like a separator file for the XML traversals
def getReviewsForISBN(isbn, clientkey, password) -> List[Review]:
    root = elementTree.fromstring(getContent(isbn, clientkey, password, CONTENTTYPE_REVIEW))

    reviewItemGenerator = [(item) for item in root.iter(tag='{http://ContentCafe2.btol.com}ReviewItem')]
    return [(Review(
        providerURI=PROVIDER_URI,
        source=reviewItem.findtext('{http://ContentCafe2.btol.com}Publication'),
        contents=reviewItem.findtext('{http://ContentCafe2.btol.com}Review')
    )) for reviewItem in reviewItemGenerator]

def getSummariesForISBN(isbn, clientkey, password) -> List[Summary]:
    root = elementTree.fromstring(getContent(isbn, clientkey, password, CONTENTTYPE_ANNOTATION))

    summaryItemGenerator = [(item) for item in root.iter(tag='{http://ContentCafe2.btol.com}AnnotationItem')]
    return [(Summary(
        providerURI=PROVIDER_URI,
        source=summaryItem.findtext('Supplier', namespaces='{http://ContentCafe2.btol.com}'),
        contents=summaryItem.findtext('{http://ContentCafe2.btol.com}Annotation')
    )) for summaryItem in summaryItemGenerator]

def getAuthorNotesForISBN(isbn, clientkey, password) -> List[AuthorNote]:
    root = elementTree.fromstring(getContent(isbn, clientkey, password, CONTENTTYPE_AUTHORNOTES))

    authorNoteGenerator = [(item) for item in root.iter(tag='{http://ContentCafe2.btol.com}BiographyItem')]
    return [(AuthorNote(
        providerURI=PROVIDER_URI,
        notes="".join([(bioItem.text)for bioItem in authorNoteitem.findall('{http://ContentCafe2.btol.com}Biography')])
    )) for authorNoteitem in authorNoteGenerator]

def getExcerptsForISBN(isbn, clientKey, password) -> List[Excerpt]:
    root = elementTree.fromstring(getContent(isbn, clientKey, password, CONTENTTYPE_EXCERPT))

    excerptGenerator = [(item) for item in root.iter(tag='{http://ContentCafe2.btol.com}ExcerptItem')]
    return [(Excerpt(
        providerURI=PROVIDER_URI,
        notes="".join([(bioItem.text) for bioItem in excerptItem.findall('{http://ContentCafe2.btol.com}Biography')])
    )) for excerptItem in excerptGenerator]

def getCoverImageInfoForISBN(clientkey, password, isbn=None):
    return getCoverImageInfo(clientkey, password, isbn)

def getCoverImageInfo(clientKey, password, isbn=None, upc=None):
    smallImageResponse = getImageLink(clientKey, password, CONTENTTYPE_SMALLCOVER, isbn, upc)
    mediumImageResponse = getImageLink(clientKey, password, CONTENTTYPE_MEDIUMCOVER, isbn, upc)
    largeImageResponse = getImageLink(clientKey, password, CONTENTTYPE_LARGECOVER, isbn, upc)

    return CoverImageInfo(
        imageType=ImageType.NONLOCAL,
        providerURI=PROVIDER_URI,
        smallImageLink = smallImageResponse.url,
        mediumImageLink = mediumImageResponse.url,
        largeImageLink = largeImageResponse.url
    )


def getContent(isbn, clientKey, password, contentType):
    contentResponse = requests.get(BASE_URI,
        params={
            'userID': clientKey,
            'password': password,
            'key': isbn,
            'content': contentType
        }
    )
    return contentResponse.content

def getImageLink(clientKey, password, coversize, isbn=None, upc=None):
    valueQueryParam = ""
    if upc is not None:
        valueQueryParam = upc
    else:
        if isbn is not None:
            valueQueryParam = isbn

    return requests.Request(
        method='GET',
        url=BASE_JACKET_URI,
        params={
            "userID": clientKey,
            "password": password,
            "Value": valueQueryParam,
            "content": coversize,
            "Return": "1",
            "Type": coversize
        }
    ).prepare()
