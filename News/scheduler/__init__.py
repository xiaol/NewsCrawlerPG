# coding: utf-8

from urllib import urlencode
from News.constans import yidianzixun
from News.constans import toutiao
from News.constans import news163
from News.scheduler import wechat


def g_queue_name(spider_name):
    return ":".join([spider_name, "start_urls"])


def g_yidianzixun_urls(channels, offset=0, end=20):
    prefix = yidianzixun.START_URL_PREFIX
    fields = ["docid", "category", "date", "image", "image_urls", "source",
              "like", "comment_count", "summary", "title", "url", "up"]
    params = {
        "path": "channel|news-list-for-keyword",
        "display": "",
        "word_type": "token",
        "fields": fields,
        "cstart": offset,
        "cend": end,
    }
    start_urls = list()
    for k, v in channels.iteritems():
        params["display"] = v
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls


def g_toutiao_urls(channels, offset=0, end=20):
    prefix = toutiao.START_URL_PREFIX
    params = {
        "source": 2,
        "offset": offset,
        "count": end,
        "utm_source": "toutiao",
    }
    start_urls = list()
    for k, v in channels.iteritems():
        params["category"] = v
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls


def g_news163_urls(channels=None, offset=0, end=20, cities=""):
    if channels is None: channels = {}
    prefix = news163.START_URL_PREFIX
    params = {
        "newchannel": "news",
        "offset": offset,
        "limit": end,
    }
    start_urls = list()
    for k, v in channels.iteritems():
        params["channel"] = v
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    for city in cities.split(","):
        params["channel"] = news163.LOCAL_CHANNEL
        params["city"] = city
        url = prefix + urlencode(params, True)
        start_urls.append(url)
    return start_urls


def g_wechat_url(name, oid):
    return wechat.get_start_url(name, oid)




