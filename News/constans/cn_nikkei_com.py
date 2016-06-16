# coding: utf-8
SPIDER_NAME = 'spider:news:cn_nikkei_com'
START_URLS = ['http://cn.nikkei.com/columnviewpoint/column.html', ]
CRAWL_SOURCE = u'日经中文网'
DOMAIN = 'nikkei.com'

ITEMS_XPATH = '//dl[@class="newsContent02"]/dt | //dl[@class="newsContent01"]/dt'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h2', 'attrs': {'class': 'style01 mB10'}}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'p', 'attrs': {'class': 'time'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'newsText fix'}}
}

EXTRACTOR_CLS = "News.extractor.NikkeiExtractor"

CATEGORIES = {
    u'专栏/观点': ('http://cn.nikkei.com/columnviewpoint/column.html', 29, 120, 3),
    u'中国游客爆买': ('http://cn.nikkei.com/top/201604-3/20227.html', 29, 120, 3),
    u'两岸观察': ('http://cn.nikkei.com/top/201604-4/20228.html', 29, 120, 3),
    u'中日深度观察': ('http://cn.nikkei.com/top/201604-2/20226.html', 29, 120, 3),
    u'南海之争': ('http://cn.nikkei.com/top/feature-uschina/20203.html', 29, 120, 3),
    u'中国': ('http://cn.nikkei.com/china.html', 29, 120, 3),
    u'专栏/观点': ('http://cn.nikkei.com/columnviewpoint.html', 29, 120, 3),
}