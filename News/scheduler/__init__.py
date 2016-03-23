# coding: utf-8

import json
from urllib import urlencode
from News.constans import CHANNELS_MAP
from News.constans import yidianzixun
from News.constans import toutiao
from News.constans import news163
from News.scheduler import wechat


def g_queue_name(spider_name):
    return ":".join([spider_name, "start_urls"])


def g_start_request(url, value):
        info = CHANNELS_MAP[value["channel"]]
        meta = dict()
        meta.update(info)
        meta.update(value)
        request = {"url": url, "meta": meta}
        return json.dumps(request)


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
    for key, value in channels.iteritems():
        params["display"] = key
        url = prefix + urlencode(params, True)
        request = g_start_request(url, value)
        start_urls.append(request)
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
    for key, value in channels.items():
        params["category"] = key
        url = prefix + urlencode(params, True)
        request = g_start_request(url, value)
        start_urls.append(json.dumps(request))
    return start_urls


def g_news163_urls(channels, offset=0, end=20):
    prefix = news163.START_URL_PREFIX
    params = {
        "newchannel": "news",
        "offset": offset,
        "limit": end,
    }
    start_urls = list()
    for key, value in channels.items():
        params["channel"] = key
        url = prefix + urlencode(params, True)
        request = g_start_request(url, value)
        start_urls.append(request)
    return start_urls


def g_news163_local_urls(cities, offset=0, end=20):
    prefix = news163.START_URL_PREFIX
    params = {
        "newchannel": "news",
        "offset": offset,
        "limit": end,
    }
    start_urls = list()
    for city in cities.split(","):
        params["channel"] = news163.LOCAL_CHANNEL
        params["city"] = city
        url = prefix + urlencode(params, True)
        request = g_start_request(url, value=news163.LOCAL_CHANNEL_VALUE)
        start_urls.append(request)
    return start_urls


def g_wechat_url(name, oid):
    return wechat.get_start_url(name, oid)




