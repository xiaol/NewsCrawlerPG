# coding: utf-8
SPIDER_NAME = 'spider:news:www_bjd_com_cn'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'京报网'
DOMAIN = 'www.bjd.com.cn'

ITEMS_XPATH = "//li/div[@class='tit'] | //li/div[@class='txt']/h1" #| //h3 | //div[@class="top_new clearfix"]/h2'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'四九城': ('http://www.bjd.com.cn/zc/sjc/', 2, 120, 3),
    u'身边事': ('http://www.bjd.com.cn/zc/sbs/', 2, 120, 4),
    u'生活圈': ('http://www.bjd.com.cn/zc/shq/', 2, 120, 3),
    u'百态图': ('http://www.bjd.com.cn/zc/btt/', 2, 120, 4),
    u'深度': ('http://www.du.bjd.com.cn/', 2, 120, 4),
    u'舞台剧': ('http://www.bjd.com.cn/pw/wtj/', 3, 120, 4),
    u'脉动': ('http://www.bjd.com.cn/pw/md/', 24, 120, 4),
    u'赏阅': ('http://www.bjd.com.cn/pw/sy/', 19, 120, 4),
}