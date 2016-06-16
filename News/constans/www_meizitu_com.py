# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 11:07"

SPIDER_NAME = "spider:news:www_meizitu_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"妹子图"
DOMAIN = "www.meizitu.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='metaRight']/h2"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"美女": ("http://www.meizitu.com/", 26, 120, 4),
}

