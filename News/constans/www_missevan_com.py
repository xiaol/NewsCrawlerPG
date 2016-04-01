# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 11:31"

SPIDER_NAME = "spider:news:www_missevan_com"
START_URLS = ["http://news.missevan.com/news/index?ntype=2"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"M新闻"
DOMAIN = "missevan.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='newsbody pie']"
TITLE_XPATH = "./div[@class='newstitle']/a/text()"
URL_XPATH = "./div[@class='newstitle']/a/@href"
SUMMARY_XPATH = "./div[@class='newscontent']/p/text()"
THUMB_XPATH = "./div[@class='newscontent']/div/a/img/@src"

TITLE_PARAM = {"name": "div", "attrs": {"id": "articletitle"}}
POST_DATE_PARAM = {"name": "div", "attrs": {"id": "articleinfo"}}
# POST_USER_PARAM = {"name": "", "attrs": {}}
# SUMMARY_PARAM = {"name": "", "attrs": {}}
CONTENT_PARAM = {"name": "div", "attrs": {"id": "articlecontent"}}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"M新闻": {
        u"动画": ("http://news.missevan.com/news/index?ntype=2", None),
        u"音乐": ("http://news.missevan.com/news/index?ntype=3", None),
        u"游戏": ("http://news.missevan.com/news/index?ntype=4", None),
        u"声优": ("http://news.missevan.com/news/index?ntype=5", None),
        u"小说": ("http://news.missevan.com/news/index?ntype=6", None),
        u"漫画": ("http://news.missevan.com/news/index?ntype=7", None),
        u"Cosplay": ("http://news.missevan.com/news/index?ntype=8", None),
        u"杂志": ("http://news.missevan.com/news/index?ntype=9", None),
        u"周边": ("http://news.missevan.com/news/index?ntype=10", None),
        u"展会": ("http://news.missevan.com/news/index?ntype=11", None),
        u"电影": ("http://news.missevan.com/news/index?ntype=12", None),
        u"萌宅": ("http://news.missevan.com/news/index?ntype=13", None),
        u"杂谈": ("http://news.missevan.com/news/index?ntype=14", None),
        u"DVD/BD": ("http://news.missevan.com/news/index?ntype=15", None),
        u"Other": ("http://news.missevan.com/news/index?ntype=16", None),
    },
}

