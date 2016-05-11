# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-01 14:14"

SPIDER_NAME = "spider:news:www_people_com_cn"
START_URLS = ["http://world.people.com.cn/GB/157278/index.html"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"人民网"
DOMAIN = "people.com.cn"

# AJAX = True
ITEMS_XPATH = "//ul[@class='list_16']/li " \
              "| //ul[@class='list_14 clearfix']/li " \
              "| //ul[@class='imp_list clearfix']/li " \
              "| //ul[@class='list_ej2  mt20']/li " \
              "| //ul[@class='list_14 list_ej']/li " \
              "| //ul[@class='list font14 ej_list list3']/li " \
              "| //ul[@class='list14']/li"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1", "attrs": {"id": "p_title"}},
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "span", "attrs": {"id": "p_publishtime"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "p_content"}},
}

EXTRACTOR_CLS = "News.extractor.PeopleExtractor"

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"时政": {
        u"高层动态": ("http://politics.people.com.cn/GB/1024/index.html", None),
        u"中央部委": ("http://politics.people.com.cn/GB/1027/index.html", None),
        u"人事任免": ("http://politics.people.com.cn/GB/41223/index.html", None),
        u"时事解读": ("http://politics.people.com.cn/GB/389979/index.html", None),
    },
    u"社会": {
        u"本网原创": ("http://society.people.com.cn/GB/86800/index.html", 2, 120, 4),
        u"民生报道": ("http://society.people.com.cn/GB/41158/index.html", None),
        u"社会万象": ("http://society.people.com.cn/GB/1062/index.html", 2, 120, 3),
    },
    u"法制": {
        u"滚动新闻": ("http://legal.people.com.cn/GB/188502/index.html", 2, 120, 3),
    },
    u"观点": {
        u"每日最新评论": ("http://opinion.people.com.cn/GB/159301/index.html", None)
    },
    u"媒体": {
        u"最新资讯": ("http://media.people.com.cn/GB/40606/index.html", None),
    },
    u"国际": {
        u"滚动新闻": ("http://world.people.com.cn/GB/157278/index.html", 9, 120, 3),
    },
    u"台湾": {
        u"滚动新闻": ("http://tw.people.com.cn/GB/104510/index.html", None),
    },
    u"财经": {
        u"滚动新闻": ("http://finance.people.com.cn/GB/70846/index.html", None),
    },
    u"IT": {
        u"滚动新闻": ("http://it.people.com.cn/GB/243510/index.html", 22, 120, 3),
    },
    u"教育": {
        u"滚动新闻": ("http://edu.people.com.cn/GB/1053/index.html", None),
    },
    u"房产": {
        u"人民出品": ("http://house.people.com.cn/GB/164291/index.html", None),
    },
    u"体育": {
        u"滚动新闻": ("http://sports.people.com.cn/GB/22176/index.html", None),
    },
    u"游戏": {
        u"滚动新闻": ("http://game.people.com.cn/GB/218877/index.html", 11, 120, 4),
    },
    u"娱乐": {
        u"独家": ("http://ent.people.com.cn/GB/233357/index.html", 3, 120, 4),
    },
    # 本地新闻待抓取
}

