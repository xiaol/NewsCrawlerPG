# coding: utf-8
SPIDER_NAME = "spider:news:22mm_xiuna_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"22MM美女"
DOMAIN = "www.22mm.xiuna.com"

# AJAX = True
ITEMS_XPATH = "//ul[@class='pic']/li"
TITLE_XPATH = "./a/@title"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#     
# }


CATEGORIES = {
    u"惊艳美女": ("http://22mm.xiuna.com/mm/jingyan/", 26, 120, 4),
    u"萝莉": ("http://22mm.xiuna.com/mm/picbest/Lolita/", 26, 120, 4),
    u"车模": ("http://22mm.xiuna.com/mm/picbest/cars/", 26, 120, 4),
}

