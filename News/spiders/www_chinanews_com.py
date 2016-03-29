# coding: utf-8

from urlparse import urljoin
from News.spiders import NewsSpider
from News.constans.www_chinanews_com import SPIDER_NAME, CRAWL_SOURCE
from News.items import get_default_news
from News.utils.util import g_cache_key, news_already_exists
from News.extractor import GeneralExtractor

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 22:03"


class ChinaNews(NewsSpider):

    name = SPIDER_NAME
    # start_urls = ["http://www.chinanews.com/china.shtml"]

    def g_news_meta_list(self, response):
        lis = response.xpath("//div[@class='content_list']//li")
        articles = list()
        for li in lis:
            article = dict()
            url = li.xpath("./div[@class='dd_bt']/a/@href").extract()
            title = li.xpath("./div[@class='dd_bt']/a/text()").extract()
            if url and title:
                article["url"] = urljoin(response.request.url, url[0])
                article["title"] = title[0]
                articles.append(article)
        return articles

    def g_news_item(self, article, start_url="", meta=None):
        crawl_url = article["url"]
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            title=article["title"],
            crawl_url=crawl_url,
            docid=crawl_url,
            key=key,
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
        )
        if meta is not None:
            news["meta_channel_id"] = meta["channel"]
            news["meta_channel_name"] = meta["name"]
            news["meta_channel_online"] = meta["online"]
        return news

    def parse_news(self, response):
        news = response.meta["news"]
        body = response.body_as_unicode().encode("utf-8")
        extractor = GeneralExtractor(body)
        post_date_param = {"name": "div", "attrs": {"class": "left-t"}}
        title, post_date, post_user, summary, content = extractor(post_date_param=post_date_param)
        news["publish_time"] = post_date
        news["content"] = content
        yield news





