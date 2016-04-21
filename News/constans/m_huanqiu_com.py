# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-31 15:50"

SPIDER_NAME = "spider:news:m_huanqiu_com"
# CLASS_NAME = ""
CRAWL_SOURCE = u"环球网"
DOMAIN = "huanqiu.com"

# AJAX = True
ITEMS_XPATH = "//div[@id='vis_listas']/div[@class='lanmu_line']"
TITLE_XPATH = "./div[@class='lanmu_line_title']/a/text()"
URL_XPATH = "./div[@class='lanmu_line_title']/a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1", "attrs": {}},
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "meta", "attrs": {"name": "publishdate"}},
}
POST_SOURCE_PARAM = {
    "method": "find_all",
    "params": {"name": "meta", "attrs": {"name": "author"}},
}
SUMMARY_PARAM = {
    "method": "find_all",
    "params": {"name": "meta", "attrs": {"name": "description"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "text"}},
}
CLEAN_CONTENT_AFTER_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'reTopics'}}
}
CLEAN_PARAM_LIST = [
    {
        'method': 'find_all',
        'params': {'name': 'img', 'attrs': {'src': 'http://a3.peoplecdn.cn/a7f5e844e54faf51ad7656367cf08c2a.jpg'}}
    }
]

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"国际": {
        u"独家报道": ("http://m.huanqiu.com/lm.html?id=33", 9, 60, 4),
        u"环球要闻": ("http://m.huanqiu.com/lm.html?id=32", 9, 60, 4),
        u"海外看中国": ("http://m.huanqiu.com/lm.html?id=35", 29, 60, 4),
    },
    u"国内": {
        u"时政要闻": ("http://m.huanqiu.com/lm.html?id=37", None),
        u"社会万象": ("http://m.huanqiu.com/lm.html?id=113", 2, 60, 3),
        # u"图说中国": ("http://m.huanqiu.com/lm.html?id=92", None), # 待解析
    },
    u"军事": {
        u"国际军事": ("http://m.huanqiu.com/lm.html?id=41", 8, 60, 3),
        u"中国军事": ("http://m.huanqiu.com/lm.html?id=40", 8, 60, 3),
        u"军事评论": ("http://m.huanqiu.com/lm.html?id=90", 8, 60, 3),
        u"航天航空": ("http://m.huanqiu.com/lm.html?id=91", 8, 60, 3),
        # u"图说军事": ("http://m.huanqiu.com/lm.html?id=43", None),　# 待解析
    },
    u"台海": {
        u"两岸时政": ("http://m.huanqiu.com/lm.html?id=44", 29, 60, 3),
        u"台湾社会": ("http://m.huanqiu.com/lm.html?id=46", 29, 60, 3),
    },
    u"评论": {
        u"环球今日评": ("http://m.huanqiu.com/lm.html?id=138", None),
        u"国际评论": ("http://m.huanqiu.com/lm.html?id=18", None),
    },
    u"财经": {
        u"中国财经": ("http://m.huanqiu.com/lm.html?id=29", 7, 60, 3),
        u"国际财讯": ("http://m.huanqiu.com/lm.html?id=48", 7, 60, 3),
    },
    u"科技": {
        u"科技资讯": ("http://m.huanqiu.com/lm.html?id=53", 22, 60, 4),
        # u"科技产品": ("http://m.huanqiu.com/lm.html?id=54", None), # 待解析
    },
    u"博览": {
        u"环球博览": ("http://m.huanqiu.com/lm.html?id=114", 9, 60, 4),
        # u"有真相": ("http://m.huanqiu.com/lm.html?id=111", None),　# 待解析
    },
    u"娱乐": {
        # u"娱乐图片": ("http://m.huanqiu.com/lm.html?id=59", None), # 待解析
    },
    u"体育": {
        u"体坛资讯": ("http://m.huanqiu.com/lm.html?id=87", None),
        # u"体坛酷图": ("http://m.huanqiu.com/lm.html?id=88", None), # 待解析
    },
    u"健康": {
        u"保健养生": ("http://m.huanqiu.com/lm.html?id=66", 24, 60, 4),
        u"健康资讯": ("http://m.huanqiu.com/lm.html?id=137", 24, 60, 4),
    },
    u"图片": {
        # u"图说世界": ("http://m.huanqiu.com/lm.html?id=62", None), # 待解析
    },
    u"时尚": {
        u"环球时尚": ("http://m.huanqiu.com/lm.html?id=163", None),
        # u"时尚视觉": ("http://m.huanqiu.com/lm.html?id=162", None), # 待解析
    },
}

