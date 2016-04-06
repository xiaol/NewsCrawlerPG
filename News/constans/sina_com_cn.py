# coding: utf-8

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-05 14:50"

SPIDER_NAME = "spider:news:sina_com_cn"
START_URLS = ["http://roll.fashion.sina.com.cn/wedding/dresses/index.shtml"]
# CLASS_NAME = ""
CRAWL_SOURCE = u"新浪网"
DOMAIN = "sina.com.cn"

# AJAX = True
ITEMS_XPATH = "//ul[@class='list_009']/li | //div[@class='bc w-list']/div[@class='blk_tw clearfix']/h3 | //div[@class='blk_tw tw01']/h2"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""

TITLE_PARAM = {
    "method": "find_all",
    "params": {"name": "h1", "attrs": {"id": "artibodyTitle"}}
}
POST_DATE_PARAM = {
    "method": "find_all",
    "params": {"name": "meta", "attrs": {"property": "article:published_time"}},
}
CONTENT_PARAM = {
    "method": "find_all",
    "params": {"name": "div", "attrs": {"id": "artibody"}},
}

# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"国内": {
        u"内地新闻": ("http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml", None),
        u"港澳台新闻": ("http://roll.news.sina.com.cn/news/gnxw/gatxw/index.shtml", None),
        u"综述分析": ("http://roll.news.sina.com.cn/news/gnxw/zs-pl/index.shtml", None),
    },
    u"国际": {
        u"环球视野": ("http://roll.news.sina.com.cn/news/gjxw/gjmtjj/index.shtml", None),
        u"环球趣闻": ("http://roll.news.sina.com.cn/news/gjxw/hqqw/index.shtml", None),
        # u"海外观察": ("http://news.sina.com.cn/gjzg/", None),  待解析
    },
    u"社会": {
        u"情感八卦": ("http://roll.news.sina.com.cn/news/shxw/zqsk/index.shtml", None),
        u"拍案说法": ("http://roll.news.sina.com.cn/news/shxw/fz-shyf/index.shtml", None),
        u"奇闻趣事": ("http://roll.news.sina.com.cn/news/shxw/qwys/index.shtml", None),
        u"五花八门": ("http://roll.news.sina.com.cn/news/shxw/shwx/index.shtml", None),
        # u"社会热图": ("http://slide.news.sina.com.cn/s/", None),　　# 待解析
    },
    u"军事": {
        # u"图片": ("http://slide.mil.news.sina.com.cn/", None),  # 待解析
        u"深度": ("http://mil.news.sina.com.cn/jssd/", None),
        u"大国博弈": ("http://mil.news.sina.com.cn/dgby/", None),
        u"军史": ("http://mil.news.sina.com.cn/jshm/", None),
    },
    u"评论": {
        # 待解析
    },
    u"体育": {
        # 待解析
    },
    u"娱乐": {
        u"明星/内地强档": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/ndqd/index.shtml", None),
        u"明星/欧美巨星": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/omjx/index.shtml", None),
        u"明星/港台风云": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/gtfy/index.shtml", None),
        u"明星/日韩偶像": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/rhox/index.shtml", None),
        u"音乐/新闻": ("http://roll.ent.sina.com.cn/ent_more/yl2/index.shtml", None),
    },
    u"财经": {
        #   待解析
    },
    u"科技": {
        #   待解析
    },
    u"时尚": {
        # u"时装/民星穿搭": ("http://roll.fashion.sina.com.cn/style/celebrity/index.shtml", None),    #　翻页
        # u"时装/潮流趋势": ("http://roll.fashion.sina.com.cn/style/trend/index.shtml", None),    # 翻页
        # u"时装/热门单品": ("http://roll.fashion.sina.com.cn/style/accessories/index.shtml", None),      # 翻页
        u"时装/时尚资讯": ("http://roll.fashion.sina.com.cn/style/info/index.shtml", None),
        # u"时装/产业观察": ("http://roll.fashion.sina.com.cn/style/industry/index.shtml", None),
        # u"时装/时尚人物": ("http://roll.fashion.sina.com.cn/style/icon1/index.shtml", None),
        # u"时装/奢华珠宝": ("http://roll.fashion.sina.com.cn/style/jewelry/index.shtml", None),
        u"时装/购物信息": ("http://roll.fashion.sina.com.cn/style/shopping/index.shtml", None),

        # u"美容/护肤": ("http://roll.fashion.sina.com.cn/beauty/skincare/index.shtml", None),
        # u"美容/彩妆": ("http://roll.fashion.sina.com.cn/beauty/makeup/index.shtml", None),
        # u"美容/美发": ("http://roll.fashion.sina.com.cn/beauty/hair/index.shtml", None),
        u"美容/资讯": ("http://roll.fashion.sina.com.cn/beauty/news/index.shtml", None),

        # u"美体/减肥瘦身": ("http://roll.fashion.sina.com.cn/body/fit/index.shtml", None),
        # u"美体/私密地带": ("http://roll.fashion.sina.com.cn/body/secret/index.shtml", None),
        # u"美体/性爱宝典": ("http://roll.fashion.sina.com.cn/body/sex/index.shtml", None),
        # u"美体/健康热点": ("http://roll.fashion.sina.com.cn/body/health/index.shtml", None),
        # u"美体/身体艺术": ("http://roll.fashion.sina.com.cn/body/tattoo/index.shtml", None),
        # u"美体/身体护理": ("http://roll.fashion.sina.com.cn/body/care/index.shtml", None),

        u"尚品/产业": ("http://roll.fashion.sina.com.cn/luxury/sinfo/index.shtml", None),
        u"尚品/豪车": ("http://roll.fashion.sina.com.cn/luxury/cars/index.shtml", None),
        # u"尚品/数码": ("http://roll.fashion.sina.com.cn/luxury/fun/index.shtml", None),   # 时间
        u"尚品/度假酒店": ("http://roll.fashion.sina.com.cn/luxury/leisure/index.shtml", None),
        u"尚品/豪宅": ("http://roll.fashion.sina.com.cn/luxury/design/index.shtml", None),
        u"尚品/游艇": ("http://roll.fashion.sina.com.cn/luxury/aeromarine/index.shtml", None),

        u"婚嫁/盛装新娘": ("http://roll.fashion.sina.com.cn/wedding/dresses/index.shtml", None),
        u"婚嫁/珠宝钻戒": ("http://roll.fashion.sina.com.cn/wedding/rings/index.shtml", None),
        u"婚嫁/婚礼殿堂": ("http://roll.fashion.sina.com.cn/wedding/ceremony/index.shtml", None),
        u"婚嫁/蜜月旅行": ("http://roll.fashion.sina.com.cn/wedding/honeymoon/index.shtml", None),
        u"婚嫁/婚恋私语": ("http://roll.fashion.sina.com.cn/wedding/relationship/index.shtml", None),
        u"婚嫁/名人婚事": ("http://roll.fashion.sina.com.cn/wedding/star/index.shtml", None),
    }
}

