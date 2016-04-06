# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-31 10:55"

SPIDER_NAME = "spider:news:www_hexun_com"
# CLASS_NAME = ""
CRAWL_SOURCE = u"和讯网"
DOMAIN = "hexun.com"

AJAX = True
ITEMS_XPATH = "result"
TITLE_XPATH = "title"
URL_XPATH = "entityurl"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "span", "attrs": {"id": "pubtime_baidu"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "artibody"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"新闻": {
        # http://news.hexun.com/domestic/
        u"国内": ("http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511056&s=30&cp=1", None),
        # http://news.hexun.com/international/
        u"国际": ("http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511065&s=30&cp=1", None)
    }
}

