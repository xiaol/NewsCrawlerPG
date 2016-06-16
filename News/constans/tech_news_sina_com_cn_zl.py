# coding: utf-8
SPIDER_NAME = 'spider:news:tech_news_sina_com_cn_zl'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'新浪网'
DOMAIN = 'www.sina.com.cn'

ITEMS_XPATH = "//div[@class='top_new clearfix']/h2 | //div[@class='feed-card-item']/h2" #| //h3 | //div[@class="top_new clearfix"]/h2'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'创事记': ('http://tech.sina.com.cn/zl/', 4, 120, 4),
    # u'互联网': ('http://tech.sina.com.cn/internet/', 4, 120, 4),
    # u'科学探索': ('http://tech.sina.com.cn/discovery/', 14, 120, 4),
}