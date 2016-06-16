# coding: utf-8
SPIDER_NAME = 'spider:news:www_mtime_com'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'时光网'
DOMAIN = 'www.mtime.com'

ITEMS_XPATH = "//div[@id='newsRegion']/ul/li/h3" #| //h3 | //div[@class="top_new clearfix"]/h2'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'热读': ('http://news.mtime.com/hot/index.html', 30, 120, 4),
}