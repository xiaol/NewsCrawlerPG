# coding: utf-8
SPIDER_NAME = "spider:news:app_myzaker_com"
# START_URLS = [""]
# CLASS_NAME = ""
CRAWL_SOURCE = u"zaker"
DOMAIN = "app.myzaker.com"

# AJAX = True
ITEMS_XPATH = "//div[@id='infinite_scroll']/a"
TITLE_XPATH = "./div/div/div/div[@class='title']/text()"
URL_XPATH = "./@href"
# SUMMARY_XPATH = ""
# THUMB_XPATH = ""


# EXTRACTOR_CLS = "News.extractor."

# CUSTOM_SETTINGS = {
#
# }


CATEGORIES = {


    u"娱乐": ("http://app.myzaker.com/index.php?app_id=9", 3, 30, 4),
    u"汽车": ("http://app.myzaker.com/index.php?app_id=7", 5, 30, 4),
    u"体育": ("http://app.myzaker.com/index.php?app_id=8", 6, 30, 4),
    u"科技": ("http://app.myzaker.com/index.php?app_id=13", 4, 30, 4),
    u"国内": ("http://app.myzaker.com/index.php?app_id=1", 2, 30, 4),
    u"国际": ("http://app.myzaker.com/index.php?app_id=2", 9, 30, 4),
    u"军事": ("http://app.myzaker.com/index.php?app_id=3", 8, 30, 4),
    u"财经": ("http://app.myzaker.com/index.php?app_id=4", 7, 30, 4),
    u"互联网": ("http://app.myzaker.com/index.php?app_id=5", 22, 30, 4),
    u"时尚": ("http://app.myzaker.com/index.php?app_id=12", 10, 30, 4),
    u"亲子": ("http://app.myzaker.com/index.php?app_id=959", 16, 30, 4),
    u"社会": ("http://app.myzaker.com/index.php?app_id=14", 2, 30, 4),
    u"科学": ("http://app.myzaker.com/index.php?app_id=1039", 14, 30, 4),
    u"奢侈品": ("http://app.myzaker.com/index.php?app_id=1067", 10, 30, 4),
    u"旅游": ("http://app.myzaker.com/index.php?app_id=981", 12, 30, 4),
    u"游戏": ("http://app.myzaker.com/index.php?app_id=10376", 11, 30, 4),
    u"电影": ("http://app.myzaker.com/index.php?app_id=10530", 30, 30, 4),
    u"理财": ("http://app.myzaker.com/index.php?app_id=11195", 7, 30, 4),
    u"健康": ("http://app.myzaker.com/index.php?app_id=10802", 24, 30, 4),
    u"美食": ("http://app.myzaker.com/index.php?app_id=10386", 15, 30, 4),

    u"命里向学": ("http://app.myzaker.com/index.php?app_id=10482", 37, 300, 4),
    u"风水玄学": ("http://app.myzaker.com/index.php?app_id=10483", 37, 300, 4),
    u"星座": ("http://app.myzaker.com/index.php?app_id=1014", 37, 100, 4),
    u"健身": ("http://app.myzaker.com/index.php?app_id=11604", 37, 100, 4),

}

