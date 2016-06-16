# coding: utf-8
SPIDER_NAME = "spider:news:www_stnn_cc"
# CLASS_NAME = ""
CRAWL_SOURCE = u"星岛环球网"
DOMAIN = "www.stnn.cc"

# AJAX = True
ITEMS_XPATH = "//ul[@class='list list-point']/li[@class='item']/a"
TITLE_XPATH = "./text()"
URL_XPATH = "./@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = "./div/a/img/@src"

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1", "attrs": {"class": "article-title"}},
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "span", "attrs": {"class": "date"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "article-content"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"海外媒体看中国": ("http://news.stnn.cc/hwmtkzg/", 29, 120, 3),
    u"台湾": ("http://news.stnn.cc/hwmtkzg/", 29, 120, 3),
}

