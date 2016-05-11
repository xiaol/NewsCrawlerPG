# coding: utf-8
SPIDER_NAME = 'spider:news:www_thepaper_cn'
START_URLS = ['http://www.thepaper.cn/channel_25951', ]
CRAWL_SOURCE = u'澎湃新闻'
DOMAIN = 'thepaper.cn'

ITEMS_XPATH = '//div[@class="news_li"]'
TITLE_XPATH = './h2/a/text()'
URL_XPATH = './div/a/@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1', 'attrs': {'class': 'news_title'}}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'news_about'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'news_txt'}}
}

# CLEAN_CONTENT_AFTER_PARAM = {
#     'method': 'find_all',
#     'params': {'name': "div", 'attrs': {'class': 'article_kuozhan'}}
# }

CATEGORIES = {
    u'长三角政商': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25491', 2, 120, 4),
    u'直击现场': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25428', 2, 120, 4),
    u'知食分子': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25464', 2, 120, 4),
    u'绿政公署': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25425', 2, 120, 4),
    u'澎湃国际': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25429', 9, 120, 4),
    u'外交学人': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25481', 9, 120, 4),
    u'澎湃防务': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25430', 8, 120, 4),
    u'浦江头条': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25422', 2, 120, 4),
    u'财经': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25951', 7, 120, 4),
    u'私家历史': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25457', 13, 120, 4),
    u'有戏': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25448', 30, 120, 4),
    u'运动家': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25599', 6, 120, 4),
    u'身体': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25942', 24, 120, 4),
    u'私奔': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=26015', 6, 120, 4),
    u'私家地理': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=25842', 12, 120, 4),
    u'亲子学堂': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=26202', 16, 120, 4),
    u'汽车圈': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=26490', 5, 120, 4),
    u'车评': ('http://www.thepaper.cn/list_masonry.jsp?nodeid=26491', 5, 120, 4),
}