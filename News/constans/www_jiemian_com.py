# coding: utf-8
SPIDER_NAME = 'spider:news:www_jiemian_com'
START_URLS = ['http://www.jiemian.com/lists/100.html', ]
CRAWL_SOURCE = u'界面'
DOMAIN = 'jiemian.com'

ITEMS_XPATH = '//div[@class="news-img"]/a'
TITLE_XPATH = './img/@alt'
URL_XPATH = './@href'
# SUMMARY_XPATH = ''

TITLE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'h1',}
}

POST_DATE_PARAM = {
    'method': 'find_all',
    'params': {'name': 'span', 'attrs': {'class': 'date'}}
}

CONTENT_PARAM = {
    'method': 'find_all',
    'params': {'name': 'div', 'attrs': {'class': 'article-content'}}
}


CATEGORIES = {
    u'国际政治': ('http://www.jiemian.com/lists/35.html', 9, 240, 4),
    u'全球经济': ('http://www.jiemian.com/lists/46.html', 7, 240, 4),
    u'中国经济': ('http://www.jiemian.com/lists/20.html', 7, 240, 4),
    u'社会民生': ('http://www.jiemian.com/lists/72.html', 2, 240, 4),
    u'每日经济分析': ('http://www.jiemian.com/lists/129.html', 7, 240, 4),
    u'大牌': ('http://www.jiemian.com/lists/25.html', 3, 240, 4),
    u'娱乐圈': ('http://www.jiemian.com/lists/76.html', 3, 240, 4),
    u'视听': ('http://www.jiemian.com/lists/77.html', 30, 240, 4),
    u'八卦': ('http://www.jiemian.com/lists/81.html', 3, 240, 4),
    u'巨星': ('http://www.jiemian.com/lists/11.html', 6, 240, 4),
    u'体育市场': ('http://www.jiemian.com/lists/78.html', 6, 240, 4),
    u'篮球': ('http://www.jiemian.com/lists/80.html', 6, 120, 4),
    u'足球': ('http://www.jiemian.com/lists/83.html', 6, 120, 4),
    u'综合': ('http://www.jiemian.com/lists/91.html', 6, 120, 4),
    u'场外': ('http://www.jiemian.com/lists/92.html', 6, 120, 4),
    u'时尚要闻': ('http://www.jiemian.com/lists/42.html', 10, 120, 4),
    u'潮流': ('http://www.jiemian.com/lists/96.html', 10, 120, 4),
    u'设计': ('http://www.jiemian.com/lists/97.html', 10, 120, 4),
    u'大咖': ('http://www.jiemian.com/lists/98.html', 10, 120, 4),
    u'美妆': ('http://www.jiemian.com/lists/99.html', 10, 120, 4),
    u'旅讯': ('http://www.jiemian.com/lists/106.html', 12, 120, 4),
    u'目的地': ('http://www.jiemian.com/lists/107.html', 12, 120, 4),
    u'游记': ('http://www.jiemian.com/lists/108.html', 12, 120, 4),
    u'行程': ('http://www.jiemian.com/lists/109.html', 12, 120, 4),
    u'必读': ('http://www.jiemian.com/lists/6.html', 4, 120, 4),
    u'趋势': ('http://www.jiemian.com/lists/43.html', 4, 120, 4),
    u'玩物': ('http://www.jiemian.com/lists/66.html', 4, 120, 4),
    u'产品榜': ('http://www.jiemian.com/lists/73.html', 4, 120, 4),
    u'生意': ('http://www.jiemian.com/lists/14.html', 5, 120, 4),
    u'座驾': ('http://www.jiemian.com/lists/57.html', 5, 120, 4),
    u'深度': ('http://www.jiemian.com/lists/7.html', 7, 120, 4),
    u'市场': ('http://www.jiemian.com/lists/64.html', 7, 120, 4),
    u'历史': ('http://www.jiemian.com/lists/131.html', 13, 120, 4),
    u'理财': ('http://www.jiemian.com/lists/5.html', 7, 120, 4),
    u'基金': ('http://www.jiemian.com/lists/87.html', 7, 120, 4),
    u'私募': ('http://www.jiemian.com/lists/88.html', 7, 120, 4),
    u'股票': ('http://www.jiemian.com/lists/89.html', 7, 120, 4),
    u'银行': ('http://www.jiemian.com/lists/94.html', 30, 120, 4),
    u'游戏要闻': ('http://www.jiemian.com/lists/100.html', 11, 120, 4),
    u'单品': ('http://www.jiemian.com/lists/119.html', 11, 120, 4),
    u'盘点': ('http://www.jiemian.com/lists/120.html', 11, 120, 4),
    u'花边趣闻': ('http://www.jiemian.com/lists/121.html', 11, 120, 4),
    u'市场特写': ('http://www.jiemian.com/lists/101.html', 7, 120, 4),
    u'调查': ('http://www.jiemian.com/lists/114.html', 7, 120, 4),
    u'军事': ('http://www.jiemian.com/lists/103.html', 8, 120, 4),
    u'金融': ('http://www.jiemian.com/lists/9.html', 7, 120, 4),
    u'消费': ('http://www.jiemian.com/lists/31.html', 7, 120, 4),
    u'每日社交热点': ('http://www.jiemian.com/lists/126.html', 18, 120, 4),
}