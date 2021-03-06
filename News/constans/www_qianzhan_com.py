# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 15:44"

SPIDER_NAME = "spider:news:www_qianzhan_com"
START_URLS = ["http://t.qianzhan.com/kuaixun/"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"前瞻网"
DOMAIN = "qianzhan.com"

# AJAX = True
ITEMS_XPATH = "//ul[@id='ul_list_news']/li[@class='open']/p[@class='tit'] | //p[@class='f22'] | //ul[@id='ulNewsList']/li/h2"
TITLE_XPATH = "./a/text()"  # 解析有问题
URL_XPATH = "./a/@href"  # 解析有问题
# SUMMARY_XPATH = "./div[@class='con']/p/text()"
# THUMB_XPATH = ""
#
# TITLE_PARAM = {
#     "method": "find_all",
#     "params": {"name": "h1", "attrs": {"id": "h_title"}},
# }
# POST_DATE_PARAM = {
#     "method": "find_all",
#     "params": {"name": "span", "attrs": {"class": "f14 blue_lighten mr10"}},
# }
# CONTENT_PARAM = {
#     "method": "find_all",
#     "params": {"name": "div", "attrs": {"class": "art"}},
# }

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"快讯": ("http://t.qianzhan.com/kuaixun/", None),
    u"风口": ("http://t.qianzhan.com/fengkou/", None),
    u"企业说": ("http://t.qianzhan.com/qiye/", 22, 120, 3),
    u"大咖": ("http://t.qianzhan.com/daka/", 22, 120, 3),
    u"科技/业界": ("http://t.qianzhan.com/ind/", 4, 120, 4),
    u"科技/互联网": ("http://t.qianzhan.com/int/", 4, 120, 4),
    u"科技/手机": ("http://t.qianzhan.com/mob/", 4, 120, 4),
    u"科技/汽车": ("http://t.qianzhan.com/car/", 5, 120, 4),
    u"科技/智能硬件": ("http://t.qianzhan.com/sma/", None),
    u"大杂会": ("http://t.qianzhan.com/dazahui/", None),

    u"明星": ('http://ent.qianzhan.com/yc/495.html', 3, 120, 4),
    u"电影": ('http://ent.qianzhan.com/yc/512.html', 30, 120, 4),
    u"电视": ('http://ent.qianzhan.com/yc/513.html', 30, 120, 4),
    u"综艺": ('http://ent.qianzhan.com/yc/515.html', 30, 120, 4),
    u"热闻": ('http://ent.qianzhan.com/list/499.html', 2, 120, 4),
    u"发现": ('http://ent.qianzhan.com/list/500.html', 31, 120, 4),
}

