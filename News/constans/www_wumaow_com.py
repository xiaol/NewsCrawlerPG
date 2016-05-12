# coding: utf-8
SPIDER_NAME = 'spider:news:www_wumaow_com'
START_URLS = ['http://www.wumaow.com', ]
CRAWL_SOURCE = u'五毛网'
DOMAIN = 'wumaow.com'

ITEMS_XPATH = '//div[@id="article"]/div[@class="post"]/div[@class="content"]/div[@class="art_right"]/h4'
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1', }
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'span', 'attrs': {'class': 'author'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'id': 'text'}}
}

EXTRACTOR_CLS = 'News.extractor.WumaowExtractor'

CATEGORIES = {
    u'首页新闻': ('http://www.wumaow.com/', 29, 120, 3),
    u'新闻': ('http://www.wumaow.com/about/', 29, 120, 3),
}