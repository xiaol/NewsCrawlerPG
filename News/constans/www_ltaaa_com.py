# coding: utf-8
SPIDER_NAME = 'spider:news:www_ltaaa_com'
START_URLS = ['http://www.ltaaa.com/wtfy.html', ]
CRAWL_SOURCE = u'龙腾网'
DOMAIN = 'ltaaa.com'

ITEMS_XPATH = '//ul[@class="wlist"]/li'
TITLE_XPATH = './div[@class="dtop"]/a/text()'
URL_XPATH = './div[@class="dtop"]/a/@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'post-title'}}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'post-param'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'post-content'}}
}


CATEGORIES = {
    u'网帖翻译': ('http://www.ltaaa.com/wtfy.html', 29, 120, 4),
}