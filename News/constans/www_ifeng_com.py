# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-30 11:10"


SPIDER_NAME = "spider:news:www_ifeng_com"
CRAWL_SOURCE = u"凤凰网"
DOMAIN = "ifeng.com"

ITEMS_XPATH = "//div[@class='juti_list'] | //div[@class='box_list clearfix']"
TITLE_XPATH = "./h3/a/@title | ./h2/a/@title"
URL_XPATH = "./h3/a/@href | ./h2/a/@href"
SUMMARY_XPATH = ".//p/text()"
# THUMB_XPATH = "./p/img/@src"

# TITLE_PARAM = {"name": None, "attrs": {}}
POST_DATE_PARAM = {"name": "p", "attrs": {"class": "p_time"}}
# POST_USER_PARAM = {"name": None, "attrs": {}}
# SUMMARY_PARAM = {"name": "p", "attrs": {"class": "art-guidecont"}}
# CONTENT_PARAM = {"name": "div", "attrs": {"class": "artile-bodycont clearfix"}}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"资讯": {
        u"大陆": ("http://news.ifeng.com/mainland/index.shtml", None),
        u"国际": ("http://news.ifeng.com/world/index.shtml", None),
        u"台湾": ("http://news.ifeng.com/taiwan/index.shtml", None),
        u"军事": ("http://news.ifeng.com/mil/index.shtml", None),  # 待解析
        u"社会": ("http://news.ifeng.com/society/index.shtml", None),
        u"图片": ("http://photo.ifeng.com/", None),  # 大图新闻, 待解析
        u"评论": ("http://news.ifeng.com/opinion/", None),  # 待解析
        u"历史": ("http://news.ifeng.com/history/", None),  # 待解析
        u"文化": ("http://culture.ifeng.com/", None),  # 待解析
        u"国学": ("http://guoxue.ifeng.com/", None),  # 待解析
    },
    u"财经": {
        # u"宏观": ("http://finance.ifeng.com/macro/", None), 待解析
    },
    u"娱乐": {
        u"明星": ("http://ent.ifeng.com/listpage/30282/1/list.shtml", None),
        u"电影": ("http://ent.ifeng.com/listpage/44169/1/list.shtml", None),
        u"电视": ("http://ent.ifeng.com/listpage/44168/1/list.shtml", None),
        u"演出": ("http://ent.ifeng.com/listpage/30741/1/list.shtml", None),
    },
    u"体育": {
        u"中国足球": ("http://sports.ifeng.com/listpage/11244/1/list.shtml", None),
        u"国际足球": ("http://sports.ifeng.com/listpage/11246/1/list.shtml", None),
        u"NBA": ("http://sports.ifeng.com/lanqiu/nba/", None),  # 待解析
        u"CBA": ("http://sports.ifeng.com/lanqiu/cba/", None),  # 待解析
        u"综合": ("http://sports.ifeng.com/listpage/11247/1/list.shtml", None),
        u"独家评论": ("http://sports.ifeng.com/listpage/54063/1/list.shtml", None),
    },
    u"时尚": {
        # 待解析
    },
    u"汽车": {
        # 待解析
    },
    u"房产": {
        # 待解析
    },
    u"科技": {
        u"互联网": ("http://tech.ifeng.com/listpage/803/1/list.shtml", None),
        u"产品": ("http://tech.ifeng.com/product/", None),  # 待解析
        u"智能家庭": ("http://tech.ifeng.com/listpage/26334/1/list.shtml", None),
        u"可穿戴&车科技": ("http://tech.ifeng.com/listpage/26335/1/list.shtml", None),
    },
    u"博报": {
        # 待解析
    },
    u"游戏": {
        # 待解析
    },
}
