# coding: utf-8
SPIDER_NAME = 'spider:news:www_waou_com_mo'
START_URLS = ['http://www.waou.com.mo/news_b/', ]
CRAWL_SOURCE = u'欧洲时报'
DOMAIN = 'waou.com.mo'
# ARTICLE_URL_TEMPLATE = ''

# ITEMS_XPATH = '//ul[@id="jgcsTable_body"]/li'
# TITLE_XPATH = './a/@title'
# URL_XPATH = './a/@href'
# # SUMMARY_XPATH = ''
#
#
#
# TITLE_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'h2',}
# }
#
# POST_DATE_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'div', 'attrs': {'class': 'gray2 f12'}}
# }
#
# CONTENT_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'div', 'attrs': {'id': 'artMain'}}
# }
#
# CLEAN_CONTENT_AFTER_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'div', 'attrs': {'class': 'mb-10 mt-10'}}
# }
#
# CATEGORIES = {
#     u'欧洲': ('http://www.oushinet.com/news/europe/', 9, 120, 4),
#     u'法媒看中国': ('http://www.oushinet.com/news/china/fmsc/', 29, 120, 4),
#     u'德媒看中国': ('http://www.oushinet.com/news/china/gmsc/', 29, 120, 4),
#     # u'中国新闻': ('http://www.zaobao.com/news/china', 29, 120, 3),
#     # u'中国财经': ('http://www.zaobao.com/finance/china', 29, 120, 3),
#     # u'财经评论/综述': ('http://www.zaobao.com/finance/comment', 29, 120, 3),
#     # u'政治经济': ('http://www.zaobao.com/wencui/politic', 29, 120, 4),
# }