# coding: utf-8
SPIDER_NAME = 'spider:news:www_ftchinese_com'
START_URLS = ['http://www.ftchinese.com/channel/china.html', ]
CRAWL_SOURCE = u'FT中文网'
DOMAIN = 'ftchinese.com'

ITEMS_XPATH = '//a[@class="thl"] | //a[@class="coverlink"]'
TITLE_XPATH = './text()'
URL_XPATH = './@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1', 'attrs': {'id': 'topictitle'}}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'a', 'attrs': {'class': 'storytime'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'content'}}
}

EXTRACTOR_CLS = "News.extractor.FTChinexeExtractor"

CATEGORIES = {
    u'中国': ('http://www.ftchinese.com/channel/china.html', 29, 120, 4),
}
