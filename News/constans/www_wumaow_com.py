# coding: utf-8
SPIDER_NAME = 'spider:news:www_wumaow_com'
START_URLS = ['http://www.wumaow.com', ]
CRAWL_SOURCE = u'五毛网'
DOMAIN = 'wumaow.com'

ITEMS_XPATH = '//div[@class="wrap"]/ul/li/div[@class="word"]/h3'
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1', }
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'span', 'class_': 'time'}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'class_': 'entry_content'}
}

EXTRACTOR_CLS = 'News.extractor.WumaowExtractor'

CATEGORIES = {
    u'首页新闻': ('http://www.wumaow.com/', 29, 120, 3),
    u'新闻': ('http://wumaow.com/category-7.html', 29, 120, 3),
}
