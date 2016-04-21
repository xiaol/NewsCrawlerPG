# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-31 17:02"

SPIDER_NAME = "spider:news:www_ifanr_com"
# START_URLS = ["http://www.ifanr.com/category/special/news"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"爱范儿"
DOMAIN = "www.ifanr.com"

# AJAX = True
# ITEMS_XPATH = "//div[@class='c-card-article__thumbnail']"
ITEMS_XPATH = "//a[@class='c-card-article__link']"
TITLE_XPATH = "./text()"
URL_XPATH = "./@href"
# SUMMARY_XPATH = "./p/text()"
# THUMB_XPATH = "./a/@href"

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1", "attrs": {"class": "entry-name"}},
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "meta", "attrs": {"name": "weibo: article:create_at"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"itemprop": "articleBody"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"汽车": ("http://www.ifanr.com/category/special/intelligentcar", 5, 60, 4),
    u"观察": ("http://www.ifanr.com/category/special/news", 22, 60, 4),
    u"新创": ("http://www.ifanr.com/category/special/innovation", 4, 60, 5),
    u"商业": ("http://www.ifanr.com/category/special/business", 4, 60, 4),
    u"MindTalk": ("http://www.ifanr.com/category/special/mindtalk", 22, 60, 4),
    u"产品": ("http://www.ifanr.com/category/special/product", 4, 60, 4),
    u"AppSolution": ("http://www.ifanr.com/app", 4, 60, 4),
    u"游戏": ("http://www.ifanr.com/category/special/game-special", 11, 60, 5),
    u"现场": ("http://www.ifanr.com/category/special/live", 4, 60, 4),
    u"译文": ("http://www.ifanr.com/category/special/%E8%AF%91%E6%96%87", 4, 60, 3),
    u"故事": ("http://www.ifanr.com/category/special/story", 22, 60, 4),
    u"清单": ("http://www.ifanr.com/category/special/%E6%B8%85%E5%8D%95", 4, 60, 3),
}

