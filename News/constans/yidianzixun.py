# coding: utf-8

SPIDER_NAME = "spider:news:yidianzixun"
CRAWL_SOURCE = u"一点资讯"
OUTER = ["jiemian.com"]
ARTICLE_URL_TEMPLATE = "http://www.yidianzixun.com/home?page=article&id={docid}"
START_URL_PREFIX = "http://www.yidianzixun.com/api/q/?"
CHANNELS = {
    "社会": {"channel": 2},
    "科技": {"channel": 4},
    "汽车": {"channel": 5},
    "体育": {"channel": 6},
    "财经": {"channel": 7},
    "军事": {"channel": 8},
    "时尚": {"channel": 10},
    "股票": {"channel": 20},
    "搞笑": {"channel": 21},
    "互联网": {"channel": 22},
    "趣图": {"channel": 23},
    "健康": {"channel": 24},
    "科学": {"channel": 25},
    "美女": {"channel": 26},
}



