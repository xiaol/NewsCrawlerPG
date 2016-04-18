# coding: utf-8

SPIDER_NAME = "spider:news:yidianzixun"
COMMENT_SPIDER_NAME = 'spider:news:comment:yidianzixun'
CRAWL_SOURCE = u"一点资讯"
OUTER = ["jiemian.com"]
ARTICLE_URL_TEMPLATE = "http://www.yidianzixun.com/article/{docid}"
START_URL_PREFIX = "http://www.yidianzixun.com/api/q/?"
CHANNELS = {
    "社会": {"channel": 2},
    "科技": {"channel": 4},
    "汽车": {"channel": 5},
    "体育": {"channel": 6},
    "财经": {"channel": 7},
    "军事": {"channel": 8},
    "时尚": {"channel": 10},
    "股票": {"channel": 20},
    "搞笑": {"channel": 21},
    "互联网": {"channel": 22},
    "趣图": {"channel": 23},
    "健康": {"channel": 24},
    "科学": {"channel": 25},
    "美女": {"channel": 26},
}

CATEGORIES = {
    u"社会": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E7%A4%BE%E4%BC%9A&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 2),
    u"科技": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E7%A7%91%E6%8A%80&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 4),
    u"汽车": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E6%B1%BD%E8%BD%A6&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 5),
    u"体育": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-channel&channel_id=7603638&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 6),
    u"财经": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E8%B4%A2%E7%BB%8F&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 7),
    u"军事": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E5%86%9B%E4%BA%8B&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 8),
    u"时尚": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E6%97%B6%E5%B0%9A&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 10),
    u"股票": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E8%82%A1%E7%A5%A8&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 20),
    u"搞笑": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E6%90%9E%E7%AC%91&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 21),
    u"互联网": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E4%BA%92%E8%81%94%E7%BD%91&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 22),
    u"趣图": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E8%B6%A3%E5%9B%BE&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 23),
    u"健康": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E5%81%A5%E5%BA%B7&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 24),
    u"科学": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-keyword&display=%E7%A7%91%E5%AD%A6&word_type=token&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 25),
    u"美女": ("http://www.yidianzixun.com/api/q/?path=channel|news-list-for-channel&channel_id=u241&fields=docid&fields=category&fields=date&fields=image&fields=image_urls&fields=like&fields=source&fields=title&fields=url&fields=comment_count&fields=summary&fields=up&cstart=0&cend=20", 26),
}

