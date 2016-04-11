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

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    "WORLDPOST": {
        u"趣闻": ("http://www.adaymag.com/worldpost/fun/", 31, 120, 4),
        u"奇闻": ("http://www.adaymag.com/worldpost/weird-news/", 31, 120, 4),
        u"温情": ("http://www.adaymag.com/worldpost/heartwarming/", 31, 120, 3),
        u"文化": ("http://www.adaymag.com/worldpost/culture/", 19, 120, 4),
        u"科学": ("http://www.adaymag.com/worldpost/science/", 14, 120, 4),
        u"女性议题": ("http://www.adaymag.com/worldpost/women/", 19, 120, 4),
        u"同性议题": ("http://www.adaymag.com/worldpost/lgbt/", None),
        u"网络热话": ("http://www.adaymag.com/worldpost/viral/", None),
    },
    "LIFESTYLE": {
        u"职场": ("http://www.adaymag.com/lifestyle/career/", None),
        u"心理,占星": ("http://www.adaymag.com/lifestyle/%E5%BF%83%E7%90%86%E5%8D%A0%E6%98%9F/", None),
        u"旅游": ("http://www.adaymag.com/lifestyle/travel/", 12, 120, 4),
        u"美食": ("http://www.adaymag.com/lifestyle/food/", 12, 120, 4),
        u"好去处": ("http://www.adaymag.com/lifestyle/things-to-do/", 12, 120, 4),
        u"宠物": ("http://www.adaymag.com/lifestyle/pet/", 32, 120, 4),
        u"健康生活": ("http://www.adaymag.com/lifestyle/healthy-live/", 24, 120, 4),
        u"两性关系": ("http://www.adaymag.com/lifestyle/love-relationship/", 19, 120, 4),
    },
    "ART&DESIGN": {
        u"设计": ("http://www.adaymag.com/art-design/design/", None),
        u"建筑": ("http://www.adaymag.com/art-design/architecture/", None),
        u"艺术": ("http://www.adaymag.com/art-design/art/", None),
        u"摄影": ("http://www.adaymag.com/art-design/photography/", 12, 120, 4),
    },
    "ENTERTAINMENT": {
        u"明星": ("http://www.adaymag.com/entertainment/celebrities/", 3, 120, 4),
        u"音乐": ("http://www.adaymag.com/entertainment/music/", None, 600, 3),   # 3
        u"电影": ("http://www.adaymag.com/entertainment/movie/", 30, 120, 4),
    },
    "FASHION": {
        # The Femin 女性时尚杂志
        # TRENDSFOLIO 男士时尚杂志
    },
}
