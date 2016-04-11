# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 15:01"


SPIDER_NAME = "spider:news:jandan_net"
CRAWL_SOURCE = u"煎蛋"
DOMAIN = "jandan.net"

ITEMS_XPATH = "//div[@id='content']//div[@class='post']"
TITLE_XPATH = "./h2[@class='title2']/a/text()"
URL_XPATH = "./h2[@class='title2']/a/@href"
# SUMMARY_XPATH = ".//span[class='hList-context']/text()"
THUMB_XPATH = "./div[@class='thumbs_b']/a/img/@data-original"

POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "time_s"}},
}
SUMMARY_PARAM = {
    "method": "find_all",
    "params": {"name": "p", "attrs": {"class": "art-guidecont"}}
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "artile-bodycont clearfix"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"科学": {
        u"走进科学": ("http://jandan.net/tag/%E8%B5%B0%E8%BF%9B%E7%A7%91%E5%AD%A6", 14, 120, 4),
        u"无厘头研究": ("http://jandan.net/tag/%E6%97%A0%E5%8E%98%E5%A4%B4%E7%A0%94%E7%A9%B6", 14, 120, 4),
        u"天文": ("http://jandan.net/tag/%E5%A4%A9%E6%96%87", 14, 120, 4),
        u"NASA": ("http://jandan.net/tag/nasa", 14, 120, 4),
        u"高科技": ("http://jandan.net/tag/%E9%AB%98%E7%A7%91%E6%8A%80", 14, 120, 4),
        u"环保": ("http://jandan.net/tag/%E7%8E%AF%E4%BF%9D", 31, 120, 4)
    },
    u"技术": {
        u"TECH": ("http://jandan.net/tag/tech", 4, 120, 4),
        u"机器人": ("http://jandan.net/tag/%E6%9C%BA%E5%99%A8%E4%BA%BA", 31, 120, 4),
        u"无人机": ("http://jandan.net/tag/%E6%97%A0%E4%BA%BA%E6%9C%BA", 4, 120, 4),
        u"3D打印": ("http://jandan.net/tag/3D%E6%89%93%E5%8D%B0", 4, 120, 4),
        u"数码产品": ("http://jandan.net/tag/%E6%95%B0%E7%A0%81%E4%BA%A7%E5%93%81", 4, 120, 4),
        u"虚拟现实": ("http://jandan.net/tag/%E8%99%9A%E6%8B%9F%E7%8E%B0%E5%AE%9E", 4, 120, 4),
    },
    u"极客": {
        u"GEEK": ("http://jandan.net/tag/GEEK", None),
        u"MEME": ("http://jandan.net/tag/MEME", None),
        u"QUORA": ("http://jandan.net/tag/quora", None),
        u"小学堂": ("http://jandan.net/tag/%E5%B0%8F%E5%AD%A6%E5%A0%82", None),
        u"创意产品": ("http://jandan.net/tag/%E5%88%9B%E6%84%8F%E4%BA%A7%E5%93%81", 31, 120, 4),
        u"WHAT IF": ("http://jandan.net/tag/whatif", None),
    },
    u"脑洞": {
        u"DIY": ("http://jandan.net/tag/DIY", None),
        u"艺术": ("http://jandan.net/tag/%E8%89%BA%E6%9C%AF", None),
        u"设计": ("http://jandan.net/tag/%E8%AE%BE%E8%AE%A1", None),
        u"广告": ("http://jandan.net/tag/%E5%B9%BF%E5%91%8A", None),
        u"建筑": ("http://jandan.net/tag/%E5%BB%BA%E7%AD%91", None),
        u"摄影": ("http://jandan.net/tag/%E6%91%84%E5%BD%B1", None),
    },
    u"故事": {
        u"冷新闻": ("http://jandan.net/tag/%E5%86%B7%E6%96%B0%E9%97%BB", 31, 180, 4),
        u"爷有钱": ("http://jandan.net/tag/%E7%88%B7%E6%9C%89%E9%92%B1", 31, 180, 3),
        u"致富信息": ("http://jandan.net/tag/%E8%87%B4%E5%AF%8C%E4%BF%A1%E6%81%AF", None),
        u"安全警示": ("http://jandan.net/tag/%E5%AE%89%E5%85%A8%E8%AD%A6%E7%A4%BA", None),
        u"国内观光": ("http://jandan.net/tag/%E5%9B%BD%E5%86%85%E8%A7%82%E5%85%89", None, 120, 1),
        u"史海钩沉": ("http://jandan.net/tag/%E5%8F%B2%E6%B5%B7%E9%92%A9%E6%B2%89", 13, 120, 4),
    },
    u"人类": {
        u"美女": ("http://jandan.net/tag/%E7%BE%8E%E5%A5%B3", 31, 120, 4),
        u"熊孩子": ("http://jandan.net/tag/%E7%86%8A%E5%AD%A9%E5%AD%90", None),
        u"大丈夫": ("http://jandan.net/tag/%E5%A4%A7%E4%B8%88%E5%A4%AB", 31, 120, 4),
        u"笨贼": ("http://jandan.net/tag/%E7%AC%A8%E8%B4%BC", 31, 120, 4),
        u"真的猛士": ("http://jandan.net/tag/%E7%9C%9F%E7%9A%84%E7%8C%9B%E5%A3%AB", 31, 120, 4),
        u"正能量": ("http://jandan.net/tag/%E6%AD%A3%E8%83%BD%E9%87%8F", 31, 120, 4),
    },
    u"折腾": {
        u"减肥": ("http://jandan.net/tag/%E5%87%8F%E8%82%A5", None),
        u"整形": ("http://jandan.net/tag/%E6%95%B4%E5%BD%A2", 31, 120, 4),
        u"变性": ("http://jandan.net/tag/%E5%8F%98%E6%80%A7", 31, 120, 3),
        u"健康": ("http://jandan.net/tag/%E5%81%A5%E5%BA%B7", 24, 120, 4),
        u"教育": ("http://jandan.net/tag/%E6%95%99%E8%82%B2", None),
        u"旅游": ("http://jandan.net/tag/%E6%97%85%E6%B8%B8", 12, 120, 4),
    },
    u"NSFW": {
        u"SEX": ("http://jandan.net/tag/sex", None),
        u"WTF": ("http://jandan.net/tag/wtf", 31, 120, 4),
        u"同性恋": ("http://jandan.net/tag/%E5%90%8C%E6%80%A7%E6%81%8B", None),
        u"重口味": ("http://jandan.net/tag/%E9%87%8D%E5%8F%A3%E5%91%B3", 31, 120, 4),
        u"何其低俗焉": ("http://jandan.net/tag/%E4%BD%95%E5%85%B6%E4%BD%8E%E4%BF%97%E7%84%89", 31, 120, 4),
        u"没品笑话集": ("http://jandan.net/tag/%E6%B2%A1%E5%93%81%E7%AC%91%E8%AF%9D%E9%9B%86", None),
    }

}
