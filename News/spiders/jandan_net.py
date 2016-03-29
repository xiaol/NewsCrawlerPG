# coding: utf-8

from urlparse import urljoin
from News.spiders import NewsSpider
from News.constans.jandan_net import SPIDER_NAME, CRAWL_SOURCE
from News.items import get_default_news
from News.utils.util import g_cache_key, news_already_exists
from News.extractor import GeneralExtractor

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 15:01"


class JanDanNet(NewsSpider):

    name = SPIDER_NAME
    start_urls = ["http://jandan.net/tag/%E8%B5%B0%E8%BF%9B%E7%A7%91%E5%AD%A6"]

    def g_news_meta_list(self, response):
        divs = response.xpath("//div[@id='content']//div[@class='post']")
        articles = list()
        for div in divs:
            article = dict()
            author = div.xpath("./div[@class='time_s']/a/text()").extract()
            thumb = div.xpath("./div[@class='thumbs_b']/a/img/@data-original").extract()
            title = div.xpath("./h2[@class='title2']/a/text()").extract()
            url = div.xpath("./h2[@class='title2']/a/@href").extract()
            if author and thumb and title and url:
                article["author"] = author[0]
                article["thumb"] = urljoin(response.request.url, thumb[0])
                article["title"] = title[0]
                article["url"] = url[0]
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
        post_date_param = {"name": "div", "attrs": {"class": "time_s"}}
        extractor = GeneralExtractor(body)
        title, post_date, post_user, summary, content = extractor(post_date_param=post_date_param)
        news["publish_time"] = post_date
        news["content"] = content
        yield news




