# coding: utf-8

import sys
from datetime import datetime
import json
from urlparse import urlparse
from News.constans.useragent import WEB_USER_AGENT
from News.extractor import GeneralExtractor
from News.extractor import WechatExtractor
from News.extractor import YiDianZiXunExtractor
from News.utils import http


def get_document(url):
    netloc = urlparse(url).netloc
    headers = {"user-agent": WEB_USER_AGENT[0],
               "host": netloc}
    r = http.get(url, headers=headers)
    if not r:
        return ''
    if r.status_code == 200:
        encoding = r.apparent_encoding
        if encoding.lower() == "gb2312":
            encoding = "GB18030"
            return r.content.decode(encoding).encode("utf-8")
        else:
            return r.content
    else:
        print("get document error: %s" % r.status_code)
        return ""


def _change_text_txt(content):
    changed = list()
    for item in content:
        for key, value in item.iteritems():
            if key == "text":
                changed.append({"txt": value})
            else:
                changed.append({key: value})
    return changed


def __change_content_compatible(content):
    old = list()
    for index, item in enumerate(content):
        old.append({str(index): item})
    return old


def test_extractor(k, url):
    string = get_document(url)
    if k == "ge":
        extractor = GeneralExtractor(string, url)
    elif k == "we":
        extractor = WechatExtractor(string, url)
    elif k == "yd":
        extractor = YiDianZiXunExtractor(string, url)
    else:
        extractor = GeneralExtractor(string, url)
    title, post_date, post_user, summary, content = extractor()
    return title, post_date, post_user, summary, content


