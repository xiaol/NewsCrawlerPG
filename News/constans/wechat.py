# coding: utf-8

SPIDER_NAME = "spider:news:wechat"
CRAWL_SOURCE = u"微信公众号"
START_URL_PREFIX = "http://weixin.sogou.com"


ID_NAME_MAPPING = {
    "16": u"外媒观光团",
    # "4": u"娱乐有话说",
}

SOURCES = [
    {"oid": "iwaimei", "name": u"外媒看天朝", "channel_id": "16"},
    # {"oid": "iQIYI2010", "name": u"爱奇艺", "channel_id": "4"},
]
