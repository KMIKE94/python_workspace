import requests
from xml.etree.ElementTree import Element
from typing import Dict, Tuple, List, Type
from syndetics.syndetics_xml import parse_xml
from syndetics.syndetics_review_sources import REVIEW_SOURCES

BASE_URI = "https://www.syndetics.com/index.aspx?isbn={isbn}&issn={issn}/{source}"
TYPE = "xw12"

# Available content sources
INDEX = "INDEX.XML"
AUTHOR_NOTES = "ANOTES.XML"
AV_SUMMARY = "AVSUMMARY.XML"
EXCERPT = "DBCHAPTER.XML"
FICTION = "FICTION.XML"
SUMMARY = "SUMMARY.XML"
SMALL_COVER = "SC.GIF"
MEDIUM_COVER = "MC.GIF"
LARGE_COVER = "LC.JPG"


# TODO: use a class for the params instead of a plain dictionary
def get_index_xml(params: Dict[str, str]) -> Element:
    return parse_xml(get_raw_response_for_source(source=INDEX, params=params))


def get_all_reviews_xml(params: Dict[str, str]) -> List[Tuple[str, Type[Element]]]:
    xml = get_index_xml(params=params)
    root = xml.find('INDEX') or xml
    sources: List[Tuple[str, str]] = [(source.text, REVIEW_SOURCES.get(source.tag, '')) for source in root.iter()
                                      if source.tag in REVIEW_SOURCES]

    return [(name, parse_xml(get_raw_response_for_source(source=file, params=params)))
            for (file, name) in sources]  # FIXME: needs more type annotations   ?


# TODO
def get_summary_xml(params: Dict[str, str]) -> Element:
    return parse_xml(get_raw_response_for_source(source=SUMMARY, params=params))


def get_author_notes_xml(params: Dict[str, str]) -> Element:
    return parse_xml(get_raw_response_for_source(source=AUTHOR_NOTES, params=params))


def get_av_summary_xml(params: Dict[str, str]) -> Element:
    return parse_xml(get_raw_response_for_source(source=AV_SUMMARY, params=params))


def get_excerpt_xml(params: Dict[str, str]) -> Element:
    return parse_xml(get_raw_response_for_source(source=EXCERPT, params=params))


def get_fiction_xml(params: Dict[str, str]) -> Element:
    return parse_xml(get_raw_response_for_source(source=FICTION, params=params))


def make_small_cover_image_url(params: Dict[str, str]) -> Element:
    return parse_xml(make_request_for_source(source=SMALL_COVER, params=params))


def make_medium_cover_image_url(params: Dict[str, str]) -> Element:
    return parse_xml(make_request_for_source(source=MEDIUM_COVER, params=params))


def make_large_cover_image_url(params: Dict[str, str]) -> Element:
    return parse_xml(make_request_for_source(source=LARGE_COVER, params=params))


# Someone please teach Syndetics how to design an API  T-T
def build_and_expand(base_uri: str, isbn: str, issn: str, source: str) -> str:
    return base_uri.replace("{isbn}", isbn).replace("{issn}", issn).replace("{source}", source)


def append_params(base_uri: str, params: Dict[str, str]) -> str:
    return base_uri + "&" + "&".join([param + "=" + value for (param, value) in params.items()])


def split_params(params: Dict[str, str]) -> Tuple[Dict[str, str], Dict[str, str]]:
    url_params_list = ['isbn', 'issn']
    other_params_list = [key for key in params.keys() if key not in url_params_list]

    url_params = {key: params.get(key, '') for key in url_params_list}
    other_params = {key: params.get(key, '') for key in other_params_list}
    other_params['type'] = TYPE
    return url_params, other_params


def make_request_for_source(source: str, params: Dict[str, str]) -> str:
    url_params, extra_params = split_params(params)
    return build_and_expand(base_uri=append_params(BASE_URI, extra_params),
                            isbn=url_params.get('isbn', ''),
                            issn=url_params.get('issn', ''),
                            source=source)


# TODO: error handling
def get_raw_response_for_source(source: str, params: Dict[str, str]) -> str:
    request_uri = make_request_for_source(source=source, params=params)
    response = requests.get(request_uri)
    return response.content
