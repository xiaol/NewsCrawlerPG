# coding: utf-8
SPIDER_NAME = 'spider:news:www_ettoday_net'
START_URLS = ['http://www.ettoday.net/news/news-list.htm', ]
CRAWL_SOURCE = u'ETtoday东森新闻云'
# DOMAIN = 'zaobao.com'
ARTICLE_URL_TEMPLATE = 'http://www.ettoday.net/news/news-list-{date}.htm'


CATEGORIES = {
    u'国际': ('http://www.ettoday.net/news/news-list/2', 9, 120, 4),
    u'政治': ('http://www.ettoday.net/news/news-list/1', 29, 120, 3),
}