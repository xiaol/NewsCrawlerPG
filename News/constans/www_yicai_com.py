# coding: utf-8
SPIDER_NAME = 'spider:news:www_yicai_com'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'第一财经'
DOMAIN = 'www.yicai.com'

ITEMS_XPATH = "//dd/h3" #| //h3 | //div[@class="top_new clearfix"]/h2'
TITLE_XPATH = './a/text() | ./span/a/text()'
URL_XPATH = './a/@href | ./span/a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'新闻': ('http://www.yicai.com/news/', 7, 120, 4),
}