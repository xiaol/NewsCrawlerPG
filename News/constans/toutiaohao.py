# coding: utf-8
SPIDER_NAME = 'spider:news:toutiaohao'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'今日头条'
DOMAIN = 'toutiao.com'

ITEMS_XPATH = "//h3" #| //h3 | //div[@class="top_new clearfix"]/h2'
TITLE_XPATH = './a/text() | ./span/a/text()'
URL_XPATH = './a/@href | ./span/a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'中国天气网': ('http://toutiao.com/m3347195657/', 38, 30, 3),
    u'囚徒健身': ('http://www.toutiao.com/m3673034792/', 24, 30, 3),
    u'火辣健身': ('http://www.toutiao.com/m4576839052/', 24, 30, 3),
    u'灵机文化': ('http://toutiao.com/m3583384386/', 37, 30, 3),
    u'易奇文化': ('http://toutiao.com/m3608654196/', 37, 30, 3),
    u'文化历史': ('http://toutiao.com/m4161860013/', 37, 30, 3),
    u'大道': ('http://toutiao.com/m4345203651/', 37, 30, 3),
    u'风水内参': ('http://www.toutiao.com/m3744976456/', 37, 30, 3),
    u'迷人推理': ('http://www.toutiao.com/m5834836226/', 37, 30, 3),
    u'风水居': ('http://toutiao.com/m5893721036/', 37, 30, 3),
}