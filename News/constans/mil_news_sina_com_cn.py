# coding: utf-8
SPIDER_NAME = 'spider:news:mil_news_sina_com_cn'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'新浪网'
DOMAIN = 'www.sina.com.cn'

AJAX = True
ITEMS_XPATH = "result|data"
TITLE_XPATH = 'title'
URL_XPATH = 'url'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'深度': ('http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=jssd&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=1&show_num=50&_=1465712256177', 8, 120, 4),
    u'军史': ('http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=lishi&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=1&show_num=50&_=1465713170883', 8, 120, 4),
    u'大国博弈': ('http://platform.sina.com.cn/news/news_list?app_key=2872801998&channel=mil&cat_1=dgby&show_all=0&show_cat=1&show_ext=1&tag=1&format=json&page=1&show_num=50&_=1465713170883', 9, 120, 4),
    u'国际派': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=10&lid=142&num=20&page=1', 9, 30, 4),
    u'国内财经': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=155&lid=1686&num=20&page=1', 7, 60, 4),
    u'产经': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=20&page=1', 7, 60, 4),
    u'券商': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=186&lid=1746&num=20&page=1', 7, 60, 4),
    u'互联网': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=204&lid=22&num=30&versionNumber=1.2.8&page=1', 22, 60, 4),
    u'健康': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=39&lid=561&num=20&versionNumber=1.2.8&page=1', 24, 60, 4),
    u'育儿': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=4&lid=12&num=30&versionNumber=1.2.8', 16, 60, 4),
    u'科学探索': ('http://feed.mix.sina.com.cn/api/roll/get?pageid=207&lid=1795&num=30&versionNumber=1.2.8&page=1', 14, 60, 4),
    u'体育': ('http://cre.dp.sina.cn/api/v3/get?feed_fmt=1&cre=sptw&mod=f&merge=3&statics=1&cateid=2L&dedup=8&offset=0&pageid=http://sports.sina.cn&lid=import&fields=url&feed_fields=url,intro,summary,wapsummary,wapurl,title,stitle,keywords,img,images,comment_total,ctime&length=110', 6, 30, 4),
    # u'滚动': ('http://roll.news.sina.com.cn/s/channel.php?ch=01#col=91&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1', 9, 30, 4), json
    # u'美股': ('http://roll.finance.sina.com.cn/s/channel.php?ch=03#col=49&spec=&type=&ch=03&k=&offset_page=0&offset_num=0&num=60&asc=&page=1', 7, 30, 4), json
    # u'娱乐': ('http://www.cankaoxiaoxi.com/photo/tstx/', 33, 120, 4), json
}