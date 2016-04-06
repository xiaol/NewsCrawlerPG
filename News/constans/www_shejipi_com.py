# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 16:17"

SPIDER_NAME = "spider:news:www_shejipi_com"
START_URLS = ["http://www.shejipi.com/"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"设计癖"
DOMAIN = "www.shejipi.com"

# AJAX = True
ITEMS_XPATH = "//article"
TITLE_XPATH = "./header/h1/a/text()"
URL_XPATH = "./header/h1/a/@href"
# SUMMARY_XPATH = ""
THUMB_XPATH = "./div/a/img/@src"

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1", "attrs": {"class": "entry-title"}},
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "span", "attrs": {"class": "date"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "entry-content"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"首页": ("http://www.shejipi.com/", None),
}

