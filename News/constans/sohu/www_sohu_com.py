# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 11:07"

SPIDER_NAME = "spider:news:www_sohu_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"搜狐体育新闻"
DOMAIN = "news.sohu.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='f14list mg10']/ul/li | //div[@class='f14list']/ul/li | //ul[@class='list-box']/li/div[@class='published']/h3/span"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"篮球": ("http://sports.sohu.com/lanqiu_a_1859.shtml", 6, 120, 4),
    u"中国足球": ("http://sports.sohu.com/guoneizuqiu_a.shtml", 6, 120, 4),
    u"国际足球": ("http://sports.sohu.com/guojizuqiu_a.shtml", 6, 120, 4),
    u"综合体育": ("http://sports.sohu.com/zonghe_a.shtml", 6, 120, 4),
    u"八卦绯闻": ("http://yule.sohu.com/stars_news.shtml", 3, 120, 4),
    u"欧美日韩明星": ("http://yule.sohu.com/star.shtml", 3, 120, 4),
    u"电影": ("http://yule.sohu.com/movie.shtml", 3, 120, 4),
    u"电视": ("http://sports.sohu.com/tv.shtml", 3, 120, 4),
    u"好莱坞": ("http://sports.sohu.com/52hollywood", 30, 120, 4),
    u"旧闻新播": ("http://history.sohu.com/jiuwenxinbo/index.shtml", 13, 120, 4),
    u"财经": ("http://it.sohu.com/yejie.shtml", 7, 120, 4),
    u"互联网": ("http://it.sohu.com/internet.shtml", 22, 120, 4),
    u"通信": ("http://it.sohu.com/tele.shtml", 4, 120, 4),
    u"智能硬件": ("http://it.sohu.com/techchanpin/index.shtml", 4, 120, 4),
    u"生活服务": ("http://it.sohu.com/shenghuo/index.shtml", 22, 120, 4),
    u"科技": ("http://it.sohu.com/yejie.shtml", 22, 120, 3),
    u"时装": ("http://fashion.sohu.com/fuzhuangs.shtml", 10, 120, 4),
    u"配饰": ("http://fashion.sohu.com/peishis.shtml", 10, 120, 4),
    u"鞋包": ("http://fashion.sohu.com/xiebaos.shtml", 10, 120, 4),
    u"孕期": ("http://baobao.sohu.com/huaiyun3.shtml", 16, 120, 4),
    u"分娩前后": ("http://baobao.sohu.com/fenmian.shtml", 16, 120, 4),
    u"准备怀孕": ("http://baobao.sohu.com/zhunbei.shtml", 16, 120, 4),
    u"亲子阅读": ("http://baobao.sohu.com/yuedu/index.shtml", 16, 120, 4),
    u"早期教育": ("http://baobao.sohu.com/baobaojiaoyu.shtml", 16, 120, 4),
    u"国内游": ("http://travel.sohu.com/china.shtml", 12, 120, 4),
    u"境外游": ("http://travel.sohu.com/shijie.shtml", 12, 120, 4),
    u"周边游": ("http://travel.sohu.com/zhoubianyou/index.shtml", 12, 120, 4),
    u"探店": ("http://chihe.sohu.com/youji/index.shtml", 15, 120, 4),
    u"食谱": ("http://chihe.sohu.com/menu/index.shtml", 15, 120, 4),
    u"佳饮": ("http://chihe.sohu.com/liquor/", 15, 120, 4),
    u"美食圈": ("http://chihe.sohu.com/experts/index.shtml", 15, 120, 4),
}

