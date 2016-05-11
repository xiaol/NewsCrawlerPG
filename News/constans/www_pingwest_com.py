# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 15:23"

SPIDER_NAME = "spider:news:www_pingwest_com"
START_URLS = ["http://www.pingwest.com/category/figure/"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"品玩"
DOMAIN = "pingwest.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='news-list']/div[@class='item']"
TITLE_XPATH = "./div[@class='item-con']/h2/a/text()"
URL_XPATH = "./div[@class='item-con']/h2/a/@href"
SUMMARY_XPATH = "./div[@class='item-con']/p/text()"
THUMB_XPATH = "./div[@class='thumb-img']/a/img/@src"

POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "span", "attrs": {"class": "post-time"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "sc-container"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"资讯": {
        u"人物": ("http://www.pingwest.com/category/figure/", 22, 120, 5),
        u"现象": ("http://www.pingwest.com/category/phenomenon/", 4, 120, 5),
        u"真相": ("http://www.pingwest.com/category/truth/", 22, 120, 4),
        u"短新闻": ("http://www.pingwest.com/category/news/", 4, 120, 4),
        u"腔调": ("http://www.pingwest.com/category/tune/", 22, 120, 4),
        u"酷玩": ("http://www.pingwest.com/category/coolplay/", 4, 120, 4),
    },
}

