# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-31 17:02"

SPIDER_NAME = "spider:news:www_ifanr_com"
START_URLS = ["http://www.ifanr.com/category/special/news"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"爱范儿"
DOMAIN = "www.ifanr.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='new-post-item-content']"
TITLE_XPATH = ".//h2/a/@title"
URL_XPATH = ".//h2/a/@href"
SUMMARY_XPATH = "./p/text()"
# THUMB_XPATH = "./a/@href"

TITLE_PARAM = {"name": "h1", "attrs": {"class": "entry-name"}}
POST_DATE_PARAM = {"name": "meta", "attrs": {"name": "weibo: article:create_at"}}
# POST_USER_PARAM = {"name": "", "attrs": {}}
# SUMMARY_PARAM = {"name": "", "attrs": {}}
CONTENT_PARAM = {"name": "div", "attrs": {"itemprop": "articleBody"}}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"汽车": ("http://www.ifanr.com/category/special/intelligentcar", None),
    u"观察": ("http://www.ifanr.com/category/special/news", None),
    u"新创": ("http://www.ifanr.com/category/special/innovation", None),
    u"商业": ("http://www.ifanr.com/category/special/business", None),
    u"MindTalk": ("http://www.ifanr.com/category/special/mindtalk", None),
    u"产品": ("http://www.ifanr.com/category/special/product", None),
    u"AppSolution": ("http://www.ifanr.com/app", None),
    u"游戏": ("http://www.ifanr.com/category/special/game-special", None),
    u"现场": ("http://www.ifanr.com/category/special/live", None),
    u"译文": ("http://www.ifanr.com/category/special/%E8%AF%91%E6%96%87", None),
    u"故事": ("http://www.ifanr.com/category/special/story", None),
    u"清单": ("http://www.ifanr.com/category/special/%E6%B8%85%E5%8D%95", None),
}

