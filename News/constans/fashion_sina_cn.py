# coding: utf-8
SPIDER_NAME = 'spider:news:fashion_sina_cn'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'新浪网'
DOMAIN = 'www.sina.com.cn'

AJAX = True
ITEMS_XPATH = "data"
TITLE_XPATH = 'title'
URL_XPATH = 'link'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'娱乐': ('http://interface.sina.cn/ent/feed.d.json?ch=fashion&col=fashion&show_num=20&page=1&act=more', 10, 60, 4),
}