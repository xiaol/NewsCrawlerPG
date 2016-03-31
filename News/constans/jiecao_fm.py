# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-31 17:56"

SPIDER_NAME = "spider:news:jiecao_fm"
START_URLS = ["http://jiecao.fm/news/"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"节操精选"
DOMAIN = "jiecao.fm"

# AJAX = True
ITEMS_XPATH = "//div[@class='list-box']/div[@class='item-box']"
TITLE_XPATH = "./a/h1/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
THUMB_XPATH = "./a/img/@src"

# TITLE_PARAM = {"name": "", "attrs": {}}
POST_DATE_PARAM = {"name": "div", "attrs": {"class": "artname pd5"}}
# POST_USER_PARAM = {"name": "", "attrs": {}}
# SUMMARY_PARAM = {"name": "", "attrs": {}}
CONTENT_PARAM = {"name": "div", "attrs": {"class": "artcontent pd5"}}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"首页": ("http://jiecao.fm/news/", None),
}

