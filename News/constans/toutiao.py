# coding: utf-8

SPIDER_NAME = "spider:news:toutiao"
COMMENT_SPIDER_NAME = "spider:news:comment:toutiao"
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

CATEGORIES = {
    u"社会": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_society&utm_source=toutiao&offset=0", 2),
    u"娱乐": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_entertainment&utm_source=toutiao&offset=0", 3),
    u"科技": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_tech&utm_source=toutiao&offset=0", 4),
    u"汽车": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_car&utm_source=toutiao&offset=0", 5),
    u"体育": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_sports&utm_source=toutiao&offset=0", 6),
    u"财经": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_finance&utm_source=toutiao&offset=0", 7),
    u"军事": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_military&utm_source=toutiao&offset=0", 8),
    u"国际": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_world&utm_source=toutiao&offset=0", 9),
    u"时尚": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_fashion&utm_source=toutiao&offset=0", 10),
    u"游戏": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_game&utm_source=toutiao&offset=0", 11),
    u"旅游": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_travel&utm_source=toutiao&offset=0", 12),
    u"历史": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_history&utm_source=toutiao&offset=0", 13),
    u"探索": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_discovery&utm_source=toutiao&offset=0", 14),
    u"美食": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_food&utm_source=toutiao&offset=0", 15),
    u"育儿": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_baby&utm_source=toutiao&offset=0", 16),
    u"养生": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_regimen&utm_source=toutiao&offset=0", 17),
    u"故事": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_story&utm_source=toutiao&offset=0", 18),
    u"美文": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_essay&utm_source=toutiao&offset=0", 19),

    u"星座": ("http://toutiao.com/api/article/recent/?source=2&count=20&category=news_astrology&utm_source=toutiao&offset=0", 37, 120, 3)
}





