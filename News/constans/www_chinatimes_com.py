# coding: utf-8

SPIDER_NAME = "spider:news:www_chinatimes_com"
CRAWL_SOURCE = u"中时电子报"
DOMAIN = "www.chinatimes.com"

ITEMS_XPATH = '//div[@class="listRight"]/ul/li/h2'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'


TITLE_PARAM = {
    'method': 'select',
    'params': {'selector': 'article header h1'}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'time'}
}

CONTENT_PARAM = {
    'method': 'select',
    'params': {'selector': 'article > article'}
}

CLEAN_CONTENT_AFTER_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'promo_word'}}
}

CUSTOM_SETTINGS = {
    "DOWNLOADER_MIDDLEWARES": {
    'News.middlewares.ProxyMiddleware': 100,
    }
}

CATEGORIES = {
    u'两岸': ('http://www.chinatimes.com/realtimenews/260409', 29, 120, 4 ),
    u'两岸2': ('http://www.chinatimes.com/realtimenews/260409?page=2', 29, 120, 4 ),
    u'两岸3': ('http://www.chinatimes.com/realtimenews/260409?page=3', 29, 120, 4 ),
    u'军事': ('http://www.chinatimes.com/realtimenews/260417', 29, 120, 4 ),
    u'军事2': ('http://www.chinatimes.com/realtimenews/260417?page=2', 29, 120, 4 ),
    u'军事3': ('http://www.chinatimes.com/realtimenews/260417?page=3', 29, 120, 4 ),
    u'中国时报(两岸国际)': ('http://www.chinatimes.com/newspapers/260108', 29, 120, 3 ),
    u'中国时报(两岸国际)2': ('http://www.chinatimes.com/newspapers/260108?page=2', 29, 120, 3 ),
    u'中国时报(两岸国际)3': ('http://www.chinatimes.com/newspapers/260108?page=3', 29, 120, 3 ),
    u'旺报': ('http://www.chinatimes.com/newspapers/2603?page=1', 29, 120, 4 ),
    u'旺报2': ('http://www.chinatimes.com/newspapers/2603?page=2', 29, 120, 4 ),
    u'旺报3': ('http://www.chinatimes.com/newspapers/2603?page=3', 29, 120, 4 ),
    u'焦点': ('http://www.chinatimes.com/realtimenews/260401', 29, 120, 3),
    u'焦点2': ('http://www.chinatimes.com/realtimenews/260401?page=2', 29, 120, 3),
    u'焦点3': ('http://www.chinatimes.com/realtimenews/260401?page=3', 29, 120, 3),
    u'热门总览': ('http://www.chinatimes.com/cn/realtimenews/hot/?page=1', 29, 120, 4 ),
    u'热门总览2': ('http://www.chinatimes.com/cn/realtimenews/hot/?page=2', 29, 120, 4 ),
    u'热门总览3': ('http://www.chinatimes.com/cn/realtimenews/hot/?page=3', 29, 120, 4 ),
}






















