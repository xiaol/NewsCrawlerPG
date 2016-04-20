# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-31 15:25"

SPIDER_NAME = "spider:news:www_hjzlg_com"
# CLASS_NAME = ""
CRAWL_SOURCE = u"韩剧资料馆"
DOMAIN = "www.hjzlg.com"

# AJAX = True
ITEMS_XPATH = "//ul[@class='list']/li"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "center"},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "size"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"韩娱新闻": ("http://www.hjzlg.com/web5/YCMS_News.asp", None),
}

