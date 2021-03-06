# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 21:24"


SPIDER_NAME = "spider:news:www_chinanews_com"
CRAWL_SOURCE = u"中国新闻网"
DOMAIN = "www.chinanews.com"

ITEMS_XPATH = "//div[@class='content_list']//li"
TITLE_XPATH = "./div[@class='dd_bt']/a/text()"
URL_XPATH = "./div[@class='dd_bt']/a/@href"
# SUMMARY_XPATH = ".//div[@class='item-details']//div[@class='td-post-text-excerpt']//text()"
# THUMB_XPATH = ".//div[@class='thumb-wrap']//img/@src"

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1', 'attrs': {'class': 'entry-title'}}
}
CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'id': 'cont_1_1_2'}}
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"class": "left-t"}},
}
CLEAN_CONTENT_BEFORE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'id': 'tupian_div'}}
}
CLEAN_CONTENT_AFTER_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'left_name'}}
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"国内": ("http://www.chinanews.com/china.shtml", 2, 20, 3),
    u"国际": ("http://www.chinanews.com/world.shtml", 9, 20, 4),
    u"军事": ("http://www.chinanews.com/mil/news.shtml", 8, 20, 4),
    u"社会": ("http://www.chinanews.com/society.shtml", 2, 20, 4),
    u"财经": ("http://finance.chinanews.com/cj/gd.shtml", 7, 20, 4),
    u"产经/房产": ("http://www.chinanews.com/house/gd.shtml", 7, 20, 3),
    u"产经/IT": ("http://it.chinanews.com/it/gd.shtml", None),  # 待添加 表内添加此源,未实现 22, 20, 4
    u"产经/能源": ("http://www.chinanews.com/energy/gd.shtml", None),
    u"金融": ("http://fortune.chinanews.com/", None),  # 待解析
    u"汽车": ("http://auto.chinanews.com/", None),  # 待解析
    u"港澳": ("http://www.chinanews.com/compatriot.shtml", 29, 20, 3),
    u"台湾": ("http://www.chinanews.com/taiwan.shtml", 29, 20, 4),
    u"华人": ("http://www.chinanews.com/huaren.shtml", 9, 20, 3),
    u"华报": ("http://www.chinanews.com/hb.shtml", 9, 20, 4),
    u"娱乐": ("http://www.chinanews.com/entertainment.shtml", 3, 20, 4),
    u"体育": ("http://www.chinanews.com/ty/gun-news.html", 6, 20, 4),
    u"文化": ("http://www.chinanews.com/wenhua.shtml", None),
    u"理论": ("http://www.chinanews.com/theory.shtml", None),
    u"生活/健康": ("http://www.chinanews.com/jiankang.shtml", None),  # 带添加
    u"游戏": ("", None),
    u"地方": ("", None),
}
