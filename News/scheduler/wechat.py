# coding: utf-8

import time
import random
import requests
from bs4 import BeautifulSoup

from News.constans.useragent import WEB_USER_AGENT


def query(keyword, page=1):
    headers = {
        "Host": "weixin.sogou.com",
        "User-Agent": random.choice(WEB_USER_AGENT),
    }
    url = "http://weixin.sogou.com/weixin"
    params = {"type": 1, "query": keyword, "ie": "utf8", "page": page}
    r = requests.get(url, params=params, headers=headers)
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
    for page in range(1, 11):
        results = query(oid, page)
        if len(results) == 0:
            results = query(name, page)
        for item in results:
            if item["name"] == name and item["oid"] == oid:
                return item["href"]
        time.sleep(random.randint(50, 150)/10.0)
    return None
