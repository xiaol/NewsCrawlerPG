# coding: utf-8

SPIDER_NAME = "spider:news:yidianzixun"
CRAWL_SOURCE = u"一点资讯"
OUTER = ["jiemian.com"]
ARTICLE_URL_TEMPLATE = "http://www.yidianzixun.com/home?page=article&id={docid}"
START_URL_PREFIX = "http://www.yidianzixun.com/api/q/?"
CHANNELS = {
    "汽车": "汽车",
    "时尚": "时尚",
    "财经": "财经",
    "趣图": "趣图",
    "健康": "健康",
    "搞笑": "搞笑",
    "互联网": "互联网",
    "军事": "军事",
    "科学": "科学",
    "股票": "股票",
    "体育": "体育",
    "科技": "科技",
    "社会": "社会",
    "美女": "美女",
}



