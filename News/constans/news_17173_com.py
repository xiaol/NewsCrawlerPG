# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 11:07"

SPIDER_NAME = "spider:news:news_17173_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"17173新闻"
DOMAIN = "news.17173.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='showlist1']/ul/li"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"全球新闻": ("http://news.17173.com/quanqiu/", 11, 120, 4),
    u"大陆新闻": ("http://news.17173.com/dalu/", 11, 120, 4),
}

