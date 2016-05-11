# coding: utf-8
SPIDER_NAME = 'spider:news:www_hanjucc_com'
START_URLS = ['http://www.hanjucc.com/hanjudongtai/list_3_3.html', ]
CRAWL_SOURCE = u'韩剧网'
DOMAIN = 'hanjucc.com'

ITEMS_XPATH = '//a[@class="title"]'
TITLE_XPATH = './text()'
URL_XPATH = './@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1',}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'details'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'contxt'}}
}


CATEGORIES = {
    u'动态': ('http://www.hanjucc.com/hanjudongtai/list_3_3.html', 30, 120, 4),
}