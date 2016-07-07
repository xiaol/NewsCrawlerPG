# coding: utf-8

import time
import random
from bs4 import BeautifulSoup
import logging

from News.constans.useragent import WEB_USER_AGENT
from News.utils import http

_logger = logging.getLogger(__file__)

def query(keyword, page=1):
    headers = {
        "Host": "weixin.sogou.com",
        "User-Agent": random.choice(WEB_USER_AGENT),
    }
    proxies = {
        "http": "127.0.0.1:3333",
        "https": "127.0.0.1:3333",
    }
    url = "http://weixin.sogou.com/weixin"
    params = {"type": 1, "query": keyword, "ie": "utf8", "page": page}
    r = None
    for i in range(3):
        r = http.get(url, params=params, headers=headers, proxies=proxies)
        if r and not (r.is_redirect or r.is_permanent_redirect):
            if r:
                _logger.warning('sogou ban')
            else:
                _logger.warning('download exception')
            break
        time.sleep(random.randint(2, 20) * 0.1)
    if not r:
        return []
    return parse(r.content)


def parse(html):
    results = list()
    soup = BeautifulSoup(html, "lxml")
    tag = soup.find("div", class_="results mt7")
    if not tag:
        return results
    for child in tag.children:
        if child.name != "div":
            continue
        href = child.get("href").strip()
        name = child.h3.get_text().strip()
        oid = child.h4.span.label.get_text().strip()
        if href and name and oid:
            results.append({"name": name, "oid": oid, "href": href})
    return results


def get_start_url(name, oid):
    results = query(oid, 1)
    for item in results:
        if item["oid"] == oid:
            return item["href"]
    return None
