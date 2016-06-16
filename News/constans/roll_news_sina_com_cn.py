# coding: utf-8
SPIDER_NAME = 'spider:news:roll_news_sina_com_cn'
# START_URLS = ['http://t.qianzhan.com/kuaixun/', ]
CRAWL_SOURCE = u'新浪新闻'
DOMAIN = 'www.sina.com.cn'

ITEMS_XPATH = "//ul[@class='list_009']/li | //ul[@class='linkNews']/li | //ul[@class='list_02']/li" #| //h3 | //div[@class="top_new clearfix"]/h2'
TITLE_XPATH = './a/text() | ./span/a/text()'
URL_XPATH = './a/@href | ./span/a/@href'
# SUMMARY_XPATH = ''



CATEGORIES = {
    u'真情时刻': ('http://roll.news.sina.com.cn/news/shxw/zqsk/index.shtml', 2, 30, 4),
    u'社会万象': ('http://roll.news.sina.com.cn/news/shxw/shwx/index.shtml', 2, 30, 4),
    u'奇闻轶事': ('http://roll.news.sina.com.cn/news/shxw/qwys/index.shtml', 2, 30, 4),
    u'社会与法': ('http://roll.news.sina.com.cn/news/shxw/fz-shyf/index.shtml', 2, 30, 4),
    u'中国军情': ('http://roll.mil.news.sina.com.cn/col/zgjq/index.shtml', 8, 60, 4),
    u'历史精选': ('http://blog.sina.com.cn/lm/history/', 13, 120, 4),
    # u'滚动': ('http://roll.news.sina.com.cn/s/channel.php?ch=01#col=91&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1', 9, 30, 4), json
    # u'美股': ('http://roll.finance.sina.com.cn/s/channel.php?ch=03#col=49&spec=&type=&ch=03&k=&offset_page=0&offset_num=0&num=60&asc=&page=1', 7, 30, 4), json
    # u'娱乐': ('http://www.cankaoxiaoxi.com/photo/tstx/', 33, 120, 4), json
}