# coding: utf-8

import json
from News.extractor import *
from News.utils.util import get_document

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 17:04"


def extract_service(k, url):
    string = get_document(url)
    if k == "ge":
        extractor = GeneralExtractor(string, url)
    elif k == "we":
        extractor = WechatExtractor(string, url)
    else:
        extractor = GeneralExtractor(string, url)
    title, post_date, post_user, summary, content = extractor(default_score_content=True)
    return title, post_date, post_user, summary, content


def score_service(url):
    string = get_document(url)
    extractor = GeneralExtractor(string, url)
    root = extractor.soup
    mapping = dict()
    score_dom_tree_new(root, mapping)
    content_tag = choose_content_tag(root, mapping)
    mapping = sorted(mapping.items(), key=lambda k: k[1], reverse=True)
    r = list()
    for tag, score in mapping:
        info = "tag:%s score:%s attrs:%s" % (tag.name, score, json.dumps(tag.attrs))
        if tag is content_tag:
            info = "<strong>" + info + "</strong>"
        r.append(info)
    return r

