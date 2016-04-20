# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 17:35"


SPIDER_NAME = "spider:news:pansci_asia"
CRAWL_SOURCE = u"PanSci 范科学"
DOMAIN = "pansci.asia"

ITEMS_XPATH = "//div[@class='list_category row']"
TITLE_XPATH = ".//div/a/@title"
URL_XPATH = ".//div/h3/a/@href"
SUMMARY_XPATH = ".//div/p/text()"
THUMB_XPATH = ".//div/a/img/@src"

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h2", "attrs": {"class": "post"}}
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "the_date"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "pure_content"}},
}
CLEAN_CONTENT_AFTER_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "wpbcap wpbcap-88960 wpbcap-app"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"内容分类": {
        u"人体解析": ("http://pansci.asia/archives/category/type/humanbeing", 24, 60, 3),
        u"地球脉动": ("http://pansci.asia/archives/category/type/earth", 14, 60, 4),
        u"自然生态": ("http://pansci.asia/archives/category/type/nature", 14, 60, 4),
        u"太空探索": ("http://pansci.asia/archives/category/type/space", 14, 60, 4),
        u"万物之理": ("http://pansci.asia/archives/category/type/%E7%89%A9%E7%90%86-%E5%8C%96%E5%AD%B8", 14, 60, 4),
        u"医疗疾病": ("http://pansci.asia/archives/category/type/medicine-disease", 24, 60, 3),
        u"文明足迹": ("http://pansci.asia/archives/category/type/%E6%96%87%E6%98%8E%E8%B6%B3%E8%B7%A1", None),
        u"环境与我": ("http://pansci.asia/archives/category/type/environment", None),
        u"生命奥秘": ("http://pansci.asia/archives/category/type/lifescience", 14, 60, 3),
        u"科学传播": ("http://pansci.asia/archives/category/type/scicomm", 14, 60, 3),
        u"科技前沿": ("http://pansci.asia/archives/category/type/technology", 4, 60, 3),
    }
}


