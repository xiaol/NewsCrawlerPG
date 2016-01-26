# coding: utf-8
from urllib import urlencode
from News.constans import yidianzixun
from News.constans import toutiao
from News.constans import news163


def g_yidianzixun_urls(close=None):
    if close is None:
        close = list()
    channels = yidianzixun.CHANNELS
    prefix = "http://www.yidianzixun.com/api/q/?"
    fields = ["docid", "category", "date", "image", "image_urls", "source",
              "like", "comment_count", "summary", "title", "url", "up"]
    params = {
        "path": "channel|news-list-for-keyword",
        "display": "",
        "word_type": "token",
        "fields": fields,
        "cstart": 0,
        "cend": 20,
    }
    start_urls = list()
    for k, v in channels:
        if k in close:
            continue
        params["display"] = v
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls


def g_toutiao_urls(close=None):
    if close is None:
        close = list()
    channels = toutiao.CHANNELS
    prefix = "http://toutiao.com/api/article/recent/?"
    params = {
        "source": 2,
        "offset": 0,
        "count": 20,
        "utm_source": "toutiao",
    }
    start_urls = list()
    for k, v in channels:
        if k in close:
            continue
        params["category"] = v
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls


def g_news163_urls(close=None):
    if close is None:
        close = list()
    close.append("本地")
    channels = news163.CHANNELS
    prefix = "http://j.news.163.com/hy/newshot.s?"
    params = {
        "newchannel": "news",
        "offset": 0,
        "limit": 30,
    }
    start_urls = list()
    for k, v in channels:
        if k in close:
            continue
        params["channel"] = v
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls


def g_news163_urls_local():
    cities = news163.CITIES.split(",")
    prefix = "http://j.news.163.com/hy/newshot.s?"
    params = {
        "newchannel": "news",
        "channel": 10,
        "offset": 0,
        "limit": 30,
    }
    start_urls = list()
    for city in cities:
        params["city"] = city
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls




