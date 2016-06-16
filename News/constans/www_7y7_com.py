# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 11:07"

SPIDER_NAME = "spider:news:www_7y7_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"七丽时尚"
DOMAIN = "www.7y7.com"

# AJAX = True
ITEMS_XPATH = "//ul[@id='piclist']/li"
TITLE_XPATH = "./a/@title"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"时尚大片": ("http://www.7y7.com/pic/dapian", 26, 120, 4),
    u"清纯美女": ("http://www.7y7.com/pic/meinv", 26, 120, 4),
}

