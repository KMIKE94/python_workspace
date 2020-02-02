from syndetics.syndetics_api import get_excerpt_xml, get_all_reviews_xml, get_summary_xml
from syndetics.syndetics_adapter import get_excerpts, get_reviews, get_summaries

PARAMS = {'isbn': '9781982110567', 'client': 'ottap'}


excerpts = get_excerpts(get_excerpt_xml(params=PARAMS))

for excerpt in excerpts:
    print(excerpt.excerpt)


for review in get_reviews(xml_with_source=get_all_reviews_xml(params=PARAMS)):
    print(review.contents)


for summary in get_summaries(get_summary_xml(params=PARAMS)):
    print(summary.contents)
