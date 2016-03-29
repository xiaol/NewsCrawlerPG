# coding: utf-8

from News.spiders import NewsSpider
from News.constans.moviesoon_com import SPIDER_NAME, CRAWL_SOURCE
from News.items import get_default_news
from News.utils.util import g_cache_key, news_already_exists
from News.extractor import GeneralExtractor

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 18:46"


class MovieSoon(NewsSpider):

    name = SPIDER_NAME
    start_urls = ["http://moviesoon.com/news/"]

    def g_news_meta_list(self, response):
        divs = response.xpath("//div[@id='content']/div[@class='post']")
        articles = list()
        for div in divs:
            article = dict()
            thumb = div.xpath("./p/img/@src").extract()
            title = div.xpath("./h2/a/text()").extract()
            url = div.xpath("./h2/a/@href").extract()
            summary = div.xpath("./p/text()").extract()
            if thumb and title and url and summary:
                article["thumb"] = thumb[0]
                article["title"] = title[0]
                article["url"] = url[0]
                article["summary"] = summary[0]
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
            summary=article["summary"]
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
        title, post_date, post_user, summary, content = extractor()
        news["content"] = content
        yield news


