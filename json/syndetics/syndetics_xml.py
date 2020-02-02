from xml.etree import ElementTree
from xml.etree.ElementTree import Element


def parse_xml(raw_response: str) -> Element:
    return ElementTree.fromstring(raw_response)
