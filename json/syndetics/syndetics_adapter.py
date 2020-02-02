from typing import List, Tuple, Type, Any
from xml.etree.ElementTree import Element

from syndetics.syndetics_api import make_small_cover_image_url, make_medium_cover_image_url, make_large_cover_image_url
from model.model import CoverImageInfo, ImageType, Review, Summary, AuthorNote, Excerpt, Subject, SubjectType

PROVIDER_SYNDETICS = "http://www.syndetics.com/"


def get_cover_image_info(isbn: str, client_key: str) -> CoverImageInfo:
    params = {'isbn': isbn, 'client_key': client_key}

    small_image = make_small_cover_image_url(params=params)
    medium_image = make_medium_cover_image_url(params=params)
    large_image = make_large_cover_image_url(params=params)

    return CoverImageInfo(type=ImageType.NONLOCAL,
                          providerURI=PROVIDER_SYNDETICS,
                          small_image=small_image,
                          medium_image=medium_image,
                          large_image=large_image)


def get_reviews(xml_with_source: List[Tuple[str, Type[Element]]]) -> List[Review]:
    review_iters = [(source, review_xml.iter('Fld520')) for (source, review_xml) in xml_with_source]
    reviews = flatten_list([[(source, review_field.find('a').text) for review_field in review_iter]
                            for (source, review_iter) in review_iters])

    return [Review(providerURI=PROVIDER_SYNDETICS,
                   contents=review_text,
                   source=source) for (source, review_text) in reviews]


def get_summaries(xml: Element) -> List[Summary]:
    summaries = [summary.find('a').text for summary in xml.iter('Fld520')]

    return [Summary(providerURI=PROVIDER_SYNDETICS, contents=summary_text) for summary_text in summaries]


def get_author_notes(xml: Element) -> List[AuthorNote]:
    notes = [noteField.find('a').text for noteField in xml.iter('Fld980')]

    return [AuthorNote(notes=noteValue, providerURI=PROVIDER_SYNDETICS) for noteValue in notes]


# FIXME, should only return one or None
def get_av_summary(xml: Element) -> List[Summary]:
    summaries = [summary.find('a').text for summary in xml.iter('Fld520')]

    return [Summary(providerURI=PROVIDER_SYNDETICS, contents=summaryValue) for summaryValue in summaries]


def get_excerpts(xml: Element) -> List[Excerpt]:
    excerpts = [excerpt.text for excerpt in xml.iter('Fld520')]

    return [Excerpt(providerURI=PROVIDER_SYNDETICS, excerpt=excerptValue) for excerptValue in excerpts]


def get_subjects(xml: Element) -> List[Subject]:
    characters = [Subject(type=SubjectType.CHARACTER,
                          heading=character.find('a').text,
                          mainTerm=character.find('f').text,
                          otherTopics=[attribute.text for attribute in character.findall('e')],
                          relationship='-'.join([character.find('g'), character.find('c')])
                          ) for character in xml.iter('Fld920')]

    time_periods = [Subject(type=SubjectType.CHRONOLOGY,
                            heading=time_period.find('c').text) for time_period in xml.iter('Fld953')]

    return characters + time_periods


def flatten_list(list_of_lists: List[Any]) -> List[Any]:
    return [y for x in list_of_lists for y in x]
