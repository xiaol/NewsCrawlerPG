# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 11:07"

SPIDER_NAME = "spider:news:www_mmonly_cc"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"唯一图库"
DOMAIN = "www.mmonly.cc"

# AJAX = True
ITEMS_XPATH = "//div[@class='title']/span"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"美女图片": ("http://www.mmonly.cc/mmtp/", 26, 120, 4),
    u"帅哥图片": ("http://www.mmonly.cc/sgtp/list_1_1.html", None),

}

