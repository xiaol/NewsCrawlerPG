# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 18:43"


SPIDER_NAME = "spider:news:moviesoon_com"
CRAWL_SOURCE = u"好莱坞电影手册"
DOMAIN = "moviesoon.com"

ITEMS_XPATH = "//div[@id='content']/div[@class='post']"
TITLE_XPATH = "./h2/a/text()"
URL_XPATH = "./h2/a/@href"
SUMMARY_XPATH = "./p/text()"
THUMB_XPATH = "./p/img/@src"

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"影像日报": ("http://moviesoon.com/news/", None)
}

