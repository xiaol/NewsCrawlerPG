# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-28 16:50"


SPIDER_NAME = "spider:news:www_adaymag_com"
CRAWL_SOURCE = "A Day Magazine"
DOMAIN = "www.adaymag.com"

ITEMS_XPATH = "//div[@class='td_mod_wrap td_mod8 ']"
TITLE_XPATH = ".//div[@class='item-details']//h3//text()"
URL_XPATH = ".//div[@class='item-details//h3/a/@href']"
SUMMARY_XPATH = ".//div[@class='item-details']//div[@class='td-post-text-excerpt']//text()"
THUMB_XPATH = ".//div[@class='thumb-wrap']//img/@src"

# TITLE_PARAM = {"name": None, "attrs": {}}
# POST_DATE_PARAM = {"name": "span", "attrs": {"id": "acreatedtime"}}
# POST_USER_PARAM = {"name": None, "attrs": {}}
# SUMMARY_PARAM = {"name": "p", "attrs": {"class": "art-guidecont"}}
# CONTENT_PARAM = {"name": "div", "attrs": {"class": "artile-bodycont clearfix"}}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    "WORLDPOST": {
        u"趣闻": ("http://www.adaymag.com/worldpost/fun/", None),
        u"奇闻": ("http://www.adaymag.com/worldpost/weird-news/", None),
        u"温情": ("http://www.adaymag.com/worldpost/heartwarming/", None),
        u"文化": ("http://www.adaymag.com/worldpost/culture/", None),
        u"科学": ("http://www.adaymag.com/worldpost/science/", None),
        u"女性议题": ("http://www.adaymag.com/worldpost/women/", None),
        u"同性议题": ("http://www.adaymag.com/worldpost/lgbt/", None),
        u"网络热话": ("http://www.adaymag.com/worldpost/viral/", None),
    },
    "LIFESTYLE": {
        u"职场": ("http://www.adaymag.com/lifestyle/career/", None),
        u"心理,占星": ("http://www.adaymag.com/lifestyle/%E5%BF%83%E7%90%86%E5%8D%A0%E6%98%9F/", None),
        u"旅游": ("http://www.adaymag.com/lifestyle/travel/", None),
        u"美食": ("http://www.adaymag.com/lifestyle/food/", None),
        u"好去处": ("http://www.adaymag.com/lifestyle/things-to-do/", None),
        u"宠物": ("http://www.adaymag.com/lifestyle/pet/", None),
        u"健康生活": ("http://www.adaymag.com/lifestyle/healthy-live/", None),
        u"两性关系": ("http://www.adaymag.com/lifestyle/love-relationship/", None),
    },
    "ART&DESIGN": {
        u"设计": ("http://www.adaymag.com/art-design/design/", None),
        u"建筑": ("http://www.adaymag.com/art-design/architecture/", None),
        u"艺术": ("http://www.adaymag.com/art-design/art/", None),
        u"摄影": ("http://www.adaymag.com/art-design/photography/", None),
    },
    "ENTERTAINMENT": {
        u"明星": ("http://www.adaymag.com/entertainment/celebrities/", None),
        u"音乐": ("http://www.adaymag.com/entertainment/music/", None),
        u"电影": ("http://www.adaymag.com/entertainment/movie/", None),
    },
    "FASHION": {
        # The Femin 女性时尚杂志
        # TRENDSFOLIO 男士时尚杂志
    },
}
