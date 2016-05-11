# coding: utf-8
# SPIDER_NAME = 'spider:news:www_wenweipo_com'
# START_URLS = ['http://news.wenweipo.com/list.php?cat=000IN&instantCat=hk', ]
# CRAWL_SOURCE = u'联合早报'
# DOMAIN = 'wenweipo.com'
#
# ITEMS_XPATH = '//a[@class="sub_fg16 "]'
# TITLE_XPATH = './text()'
# URL_XPATH = './@href'
# # SUMMARY_XPATH = ''
#
# TITLE_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'h1', 'attrs': {'itemprop': 'headline'}}
# }
#
# POST_DATE_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'font', 'attrs': {'class': 'sub_fg12'}}
# }
#
# CONTENT_PARAM = {
#     'method': 'find_all',
#     'params': {'name': 'td', 'attrs': {'align': 'left'}}
# }
#
# # CLEAN_CONTENT_AFTER_PARAM = {
# #     'method': 'find_all',
# #     'params': {'name': 'div', 'attrs': {'class': 'two_column_div'}}
# # }
#
# CATEGORIES = {
#     u'中国新闻': ('http://www.zaobao.com/news/china', 29, 120, 3),
#     u'中国财经': ('http://www.zaobao.com/finance/china', 29, 120, 3),
#     u'财经评论/综述': ('http://www.zaobao.com/finance/comment', 29, 120, 3),
#     u'政治经济': ('http://www.zaobao.com/wencui/politic', 29, 120, 4),
# }