# coding: utf-8

SPIDER_NAME = "spider:news:toutiao"
CRAWL_SOURCE = u"今日头条"
DOMAIN = "http://toutiao.com"
OUTER = ["jiemian.com", "mafengwo.cn"]
START_URL_PREFIX = "http://toutiao.com/api/article/recent/?"
CHANNELS = {
    "news_society": {"channel": 2},
    "news_entertainment": {"channel": 3},
    "news_tech": {"channel": 4},
    "news_car": {"channel": 5},
    "news_sports": {"channel": 6},
    "news_finance": {"channel": 7},
    "news_military": {"channel": 8},
    "news_world": {"channel": 9},
    "news_fashion": {"channel": 10},
    "news_game": {"channel": 11},
    "news_travel": {"channel": 12},
    "news_history": {"channel": 13},
    "news_discovery": {"channel": 14},
    "news_food": {"channel": 15},
    "news_baby": {"channel": 16},
    "news_regimen": {"channel": 17},
    "news_story": {"channel": 18},
    "news_essay": {"channel": 19},
}





