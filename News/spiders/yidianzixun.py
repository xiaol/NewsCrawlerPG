# coding: utf-8

from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data
from News.items import NewsItem
from News.constans.yidianzixun import SPIDER_NAME
from News.constans.yidianzixun import ARTICLE_URL_TEMPLATE
from News.constans.yidianzixun import CRAWL_SOURCE
from News.extractor.yidianzixun import YiDianZiXunExtractor


class YiDianZiXun(NewsSpider):

    name = SPIDER_NAME

    def parse(self, response):
        data = load_json_data(response.body)
        articles = data.get("result", [])
        for article in articles:
            item = self.g_news_item(article)
            if item is not None:
                yield self.g_news_request(item)

    def g_news_item(self, article):
        news = NewsItem()
        if article["ctype"] != "news": return None  # fixme: only support news now
        news["docid"] = article["docid"]
        news["crawl_url"] = self._g_article_url(news["docid"])
        news["key"] = self.g_cache_key(news["crawl_url"])
        if self.news_already_exists(news["key"]): return None
        news["title"] = article["title"]
        news["tags"] = list()
        news["summary"] = article.get("summary", "")
        news["publish_time"] = article["date"]
        news["content"] = list()
        news["province"] = news["city"] = news["district"] = None
        news["love"] = article.get("like", 0)
        news["up"] = article.get("up", 0)
        news["down"] = 0

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
        if "window.location.replace" in response.body:
            news["crawl_url"] = news["original_url"]
            news["key"] = self.g_cache_key(news["crawl_url"])
            yield self.g_news_request(news)
        else:
            redirects = response.request.meta.get("redirect_urls")
            if redirects:
                news["crawl_url"] = response.url
                news["key"] = self.g_cache_key(news["crawl_url"])
            extractor = YiDianZiXunExtractor(response.body, response.url, news=news)
            content, image_number = extractor.extract()
            news["content"] = content
            news["image_number"] = image_number
            yield news

    @staticmethod
    def _g_article_url(docid):
        return ARTICLE_URL_TEMPLATE.format(docid=docid)




