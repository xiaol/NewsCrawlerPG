# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 11:32"


SPIDER_NAME = "spider:news:i_cri_cn"
CRAWL_SOURCE = u"国际在线"
DOMAIN = "cri.cn"

CATEGORIES = {
    u"国际": ("http://i.cri.cn/world", None),
    u"国内": ("http://i.cri.cn/china", None),
    u"趣闻": ("http://i.cri.cn/popularnews", None),
    u"财经": ("http://i.cri.cn/finance", None),
    u"评论": ("http://i.cri.cn/opinion", None),
}
