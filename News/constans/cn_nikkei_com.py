# coding: utf-8
SPIDER_NAME = 'spider:news:cn_nikkei_com'
START_URLS = ['http://cn.nikkei.com/columnviewpoint/column.html', ]
CRAWL_SOURCE = u'日经中文网'
DOMAIN = 'nikkei.com'

ITEMS_XPATH = '//dl[@class="newsContent02"]/dt'
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
}