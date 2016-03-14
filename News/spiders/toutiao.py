# coding: utf-8

from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.utils.util import str_from_timestamp
from News.items import NewsItem
from News.constans.toutiao import SPIDER_NAME
from News.constans.toutiao import DOMAIN
from News.constans.toutiao import CRAWL_SOURCE
from News.extractor.toutiao import TouTiaoExtractor


class TouTiao(NewsSpider):

    name = SPIDER_NAME

    def parse(self, response):
        data = load_json_data(response.body)
        articles = data.get("data", [])
        for article in articles:
            item = self.g_news_item(article)
            if item is not None:
                yield self.g_news_request(item)

    def g_news_item(self, article):
        news = NewsItem()
        if article.get("has_video"): return None
        news["docid"] = article["source_url"]
        news["crawl_url"] = self._g_crawl_url(news["docid"])
        news["key"] = g_cache_key(news["crawl_url"])
        if news_already_exists(news["key"]): return None
        news["title"] = article["title"]
        news["tags"] = article.get("keywords", "").split(",")
        news["summary"] = article.get("abstract", "")
        news["publish_time"] = str_from_timestamp(article["publish_time"])
        news["content"] = list()
        news["province"] = news["city"] = news["district"] = None
        news["love"] = article.get("favorite_count", 0)
        news["up"] = article.get("digg_count", 0)
        news["down"] = article.get("bury_count", 0)
        news["image_list"] = self._g_image_list(article)

        news["original_url"] = article.get("url", "")
        news["channel"] = ""
        news["category"] = ""
        news["crawl_source"] = CRAWL_SOURCE
        news["original_source"] = article.get("source", "")
        return news

    def g_news_request(self, item):
        url = item["crawl_url"]
        return Request(
            url=url,
            callback=self.parse_news,
            meta={"news": item}
        )

    def parse_news(self, response):
        news = response.meta["news"]
        redirects = response.request.meta.get("redirect_urls")
        if redirects:
            news["crawl_url"] = response.url
            news["key"] = g_cache_key(news["crawl_url"])
        extractor = TouTiaoExtractor(response.body, response.url, news=news)
        content, image_number = extractor.extract()
        news["content"] = content
        news["image_number"] = image_number
        yield news

    @staticmethod
    def _g_crawl_url(path):
        return DOMAIN + path

    @staticmethod
    def _g_image_list(article):
        urls = [item["url"] for item in article["image_list"] if "url" in item]
        if not urls and article.get("image_url"):
            urls.append(article["image_url"])
        return urls





