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

CATEGORIES = {
    u"国内": ("http://www.chinanews.com/china.shtml", None),
    u"国际": ("http://www.chinanews.com/world.shtml", None),
    u"军事": ("http://www.chinanews.com/mil/news.shtml", None),
    u"社会": ("http://www.chinanews.com/society.shtml", None),
    u"财经": ("http://finance.chinanews.com/cj/gd.shtml", None),
    u"产经/房产": ("http://www.chinanews.com/house/gd.shtml", None),
    u"产经/IT": ("http://it.chinanews.com/it/gd.shtml", None),  # 待添加
    u"产经/能源": ("http://www.chinanews.com/energy/gd.shtml", None),
    u"金融": ("http://fortune.chinanews.com/", None),  # 待解析
    u"汽车": ("http://auto.chinanews.com/", None),  # 待解析
    u"港澳": ("http://www.chinanews.com/compatriot.shtml", None),
    u"台湾": ("http://www.chinanews.com/taiwan.shtml", None),
    u"华人": ("http://www.chinanews.com/huaren.shtml", None),
    u"华报": ("http://www.chinanews.com/hb.shtml", None),
    u"娱乐": ("http://www.chinanews.com/entertainment.shtml", None),
    u"体育": ("http://www.chinanews.com/ty/gun-news.html", None),
    u"文化": ("http://www.chinanews.com/wenhua.shtml", None),
    u"理论": ("http://www.chinanews.com/theory.shtml", None),
    u"生活/健康": ("http://www.chinanews.com/jiankang.shtml", None),  # 带添加
    u"游戏": ("", None),
    u"地方": ("", None),
}
