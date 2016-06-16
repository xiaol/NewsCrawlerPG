# coding: utf-8
SPIDER_NAME = 'spider:news:www_cankaoxiaoxi_com'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'参考消息'
DOMAIN = 'www.cankaoxiaoxi.com'

ITEMS_XPATH = '//h3[@class="YH"]'
TITLE_XPATH = './a/text()'
URL_XPATH = './a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'中国': ('http://china.cankaoxiaoxi.com/', 29, 120, 4),
    u'国际': ('http://world.cankaoxiaoxi.com/', 29, 120, 3),
    u'财经': ('http://finance.cankaoxiaoxi.com/', 29, 120, 4),
    u'台海': ('http://tw.cankaoxiaoxi.com/', 29, 120, 4),
    u'科技健康': ('http://science.cankaoxiaoxi.com/', 29, 120, 3),
    u'观点.专栏': ('http://column.cankaoxiaoxi.com/', 29, 120, 4),
    u'图说24小时': ('http://www.cankaoxiaoxi.com/photo/tstx/', 33, 120, 4),
}