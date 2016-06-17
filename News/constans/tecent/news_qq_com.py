# coding: utf-8
SPIDER_NAME = "spider:news:news_qq_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"腾讯网"
DOMAIN = "news.qq.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='list first']/div/div/div/em | //div[@class='Q-tpWrap']/em"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"国际": ("http://news.qq.com/world_index.shtml", 9, 120, 4),
    u"社会": ("http://news.qq.com/society_index.shtml", 2, 120, 4),
    u"军事": ("http://mil.qq.com/mil_index.htm", 8, 120, 4),
}

