# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-30 16:47"

SPIDER_NAME = "spider:news:www_gq_com_cn"
# CLASS_NAME = ""
CRAWL_SOURCE = u"GQ男士网"
DOMAIN = "www.gq.com.cn"

ITEMS_XPATH = "//div[@class='ThList-cont clearfix']"
TITLE_XPATH = "./a/@title"
URL_XPATH = "./a/@href"
SUMMARY_XPATH = ".//span[class='hList-context']/text()"
THUMB_XPATH = "./a/img/@src"

# TITLE_PARAM = {"name": None, "attrs": {}}
POST_DATE_PARAM = {"name": "p", "attrs": {"class": "author-box clearfix"}}
# POST_USER_PARAM = {"name": None, "attrs": {}}
SUMMARY_PARAM = {"name": "p", "attrs": {"class": "art-guidecont"}}
CONTENT_PARAM = {"name": "div", "attrs": {"class": "artile-bodycont clearfix"}}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"好玩": {
        u"GQ雷达": ("http://www.gq.com.cn/fun/radar/", None),
        u"玩意儿": ("http://www.gq.com.cn/fun/cool-stuff/", None),
        u"GQ研究": ("http://www.gq.com.cn/fun/research/", None),
        u"数据": ("http://www.gq.com.cn/fun/data/", None),
        u"绯闻男人": ("http://www.gq.com.cn/fun/gossip/", None),
        u"语录": ("http://www.gq.com.cn/fun/quote/", None),
    },
    u"潮流": {
        u"男装秀场": ("http://shows.gq.com.cn/", None),
        u"搭配指南": ("http://www.gq.com.cn/fashion/dressing-tips/", None),
        u"流行趋势": ("http://www.gq.com.cn/fashion/trends/", None),
        u"必备单品": ("http://www.gq.com.cn/fashion/item/", None),
        u"时尚圈": ("http://www.gq.com.cn/fashion/news/", None),
    },
    u"腕表": {
        u"新品资讯": ("http://www.gq.com.cn/watch/news/", None),
        u"购表指南": ("http://www.gq.com.cn/watch/guide/", None),
        u"腕表词典": ("http://www.gq.com.cn/watch/wiki/", None),
        u"名家名表": ("http://www.gq.com.cn/watch/collection/", None),
    },
    u"汽车": {
        u"玩家": ("http://www.gq.com.cn/auto/player/", None),
        u"装备": ("http://www.gq.com.cn/auto/equipment/", None),
        u"探索": ("http://www.gq.com.cn/auto/discover/", None),
        u"印象": ("http://www.gq.com.cn/auto/image/", None),
    },
    u"数码": {
        # 待解析
    },
    u"生活": {
        u"吃喝享乐": ("http://www.gq.com.cn/living/leisure/", None),
        u"型男保养": ("http://www.gq.com.cn/living/grooming/", None),
        u"运动健身": ("http://www.gq.com.cn/living/fitness/", None),
        u"性情男人": ("http://www.gq.com.cn/living/dating-and-sex/", None),
        u"CNI餐厅": ("http://www.gq.com.cn/living/cnirestaurants/", None),
        u"职场Boost": ("http://www.gq.com.cn/living/condenastcenter/", None),
    },
    u"女人": {
        # 待解析
    },
    u"人物": {
        u"年度人物": ("http://www.gq.com.cn/tag/91167", None),
    },
}

