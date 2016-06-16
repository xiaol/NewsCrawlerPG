# coding: utf-8
SPIDER_NAME = "spider:news:www_4908_cn"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"奇趣网"
DOMAIN = "www.4908.com"

# AJAX = True
ITEMS_XPATH = "//div[@class='summary']/h3"
TITLE_XPATH = "./a/text()"
URL_XPATH = "./a/@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {
    u"奇趣动物": ("http://www.4908.cn/html/Animals/", 31, 30, 4),
    u"趣闻轶事": ("http://www.4908.cn/html/QuWenYiShi/", 31, 30, 4),
    u"世界之最": ("http://www.4908.cn/html/ShiJieZhiZui/", 31, 30, 3),
    u"科学探秘": ("http://www.4908.cn/html/YuZhou/", 14, 120, 4),
    u"野史逸闻": ("http://www.4908.cn/html/YeShiYiWen/", 13, 120, 4),
    u"热点扫描": ("http://www.4908.cn/html/SheHuiReDian/", 2, 120, 3),
}

