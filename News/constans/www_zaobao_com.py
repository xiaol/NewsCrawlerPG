# coding: utf-8
SPIDER_NAME = 'spider:news:www_zaobao_com'
START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'联合早报'
DOMAIN = 'zaobao.com'

ITEMS_XPATH = '//h1[@class="title heading_article_headlines"]'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1', 'attrs': {'itemprop': 'headline'}}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'p', 'attrs': {'class': 'time'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'id': 'article_content'}}
}

CLEAN_CONTENT_AFTER_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'two_column_div'}}
}

CATEGORIES = {
    u'中国新闻': ('http://www.zaobao.com/news/china', 29, 120, 3),
    u'中国财经': ('http://www.zaobao.com/finance/china', 29, 120, 3),
    u'财经评论/综述': ('http://www.zaobao.com/finance/comment', 29, 120, 3),
    u'政治经济': ('http://www.zaobao.com/wencui/politic', 29, 120, 4),
}