# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 10:55"

SPIDER_NAME = "spider:news:www_jrj_com_cn"
START_URLS = ["http://finance.jrj.com.cn/list/guoneicj.shtml"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"金融界"
DOMAIN = "jrj.com.cn"

# AJAX = True
ITEMS_XPATH = "//ul[@class='list2']/li"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "p", "attrs": {"class": "inftop"}},
}
SUMMARY_PARAM = {
    "method": "find_all",
    "params": {"name": "meta", "attrs": {"name": "description"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "texttit_m1"}},
}
CLEAN_CONTENT_BEFORE_PARAM = {
    "method": "find_all",
    "params": {"name": "p", "class_": "linknew"}
}
# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"财经频道": {
        u"国内财经": ("http://finance.jrj.com.cn/list/guoneicj.shtml", 7, 60, 3),
        u"国际财经": ("http://finance.jrj.com.cn/list/guojicj.shtml", 7, 60, 3),
        u"产业动态": ("http://finance.jrj.com.cn/list/industrynews.shtml", 7, 60, 3),
        u"微学院": ("http://finance.jrj.com.cn/list/weixx.shtml", 20, 60, 3),
    },
    u"观点": {
        u"名家专栏": ("http://opinion.jrj.com.cn/list/mjzl.shtml", 20, 60, 3),
        u"谈股论金": ("http://opinion.jrj.com.cn/list/tglj.shtml", 20, 60, 3),
        u"经济时评": ("http://opinion.jrj.com.cn/list/jjsp.shtml", 7, 60, 4),
        u"产业观察": ("http://opinion.jrj.com.cn/list/cygc.shtml", 7, 60, 3),
    },
}

