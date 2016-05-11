# coding: utf-8
SPIDER_NAME = 'spider:news:www_hanjumi_net'
START_URLS = ['http://www.hanjumi.net/hanjuxinwen/', ]
CRAWL_SOURCE = u'韩剧迷'
DOMAIN = 'hanjumi.net'

ITEMS_XPATH = '//ul[@class="lists"]/li'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1',}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'article_title'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'content'}}
}

CLEAN_CONTENT_AFTER_PARAM = {
    'method': 'find_all',
    'params': {'name': "div", 'attrs': {'class': 'article_kuozhan'}}
}

CATEGORIES = {
    u'韩剧资讯': ('http://www.hanjumi.net/hanjuxinwen/', 30, 120, 4),
    u'电影资讯': ('http://www.hanjumi.net/hanguodianyingxinwen/', 30, 120, 4),
    u'综艺资讯': ('http://www.hanjumi.net/zongyixinwen/', 30, 120, 4),
}