# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 11:07"

SPIDER_NAME = "spider:news:news_sohu_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"搜狐新闻"
DOMAIN = "news.sohu.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='article-list']"
TITLE_XPATH = "./div/h3/a/text()"
URL_XPATH = "./div/h3/a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1"}
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "time-source"}}
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "contentText"}}
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"民调": {
        u"国内": ("http://news.sohu.com/guoneixinwen.shtml", None),
        u"国际": ("http://news.sohu.com/guojixinwen.shtml", None),
    }
}

