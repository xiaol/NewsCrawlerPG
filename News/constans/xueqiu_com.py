# coding: utf-8
SPIDER_NAME = 'spider:news:xueqiu_com'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'雪球'
DOMAIN = 'xueqiu.com'

AJAX = True
ITEMS_XPATH = ""
TITLE_XPATH = 'title'
URL_XPATH = 'url'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'沪深': ('https://xueqiu.com/today/cn', 8, 120, 4),
}
