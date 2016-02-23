# coding: utf-8

from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data
from News.items import NewsItem
from News.constans.wechat import SPIDER_NAME
from News.constans.wechat import CRAWL_SOURCE


class Wechat(NewsSpider):

    name = SPIDER_NAME

    def parse(self, response):
        results = load_json_data(response.body)
        total = int(results["totalPages"])
        page = int(results["page"])
        articles = results["items"]
        for article in articles:
            item = self.g_news_item(article, response.request.url)
            if item is not None:
                yield self.g_news_request(item)

    def g_news_item(self, article, start_url=""):
        news = NewsItem()
        news["docid"] = ""
        crawl_url = self._g_crawl_url(article)
        if not crawl_url: return None
        print crawl_url
        news["crawl_url"] = crawl_url
        news["key"] = self.g_cache_key(crawl_url)
        news["title"] = ""
        news["tags"] = list()
        news["summary"] = ""
        news["publish_time"] = ""
        news["content"] = list()
        news["province"] = None
        news["city"] = None
        news["district"] = None
        news["love"] = 0
        news["up"] = 0
        news["down"] = 0
        news["image_list"] = list()

        news["original_url"] = ""
        news["channel"] = ""
        news["crawl_source"] = CRAWL_SOURCE
        news["original_source"] = ""

        news["start_url"] = start_url
        return news

    def g_news_request(self, item):
        url = item["crawl_url"]
        return Request(
            url=url,
            callback=self.parse_news,
            meta={"news": item}
        )

    def parse_news(self, response):
        print response.body

    @staticmethod
    def _g_crawl_url(string):
        domain = "http://weixin.sogou.com"
        start = string.find("<url><![CDATA[")
        end = string.find("]]></url>")
        if start > 0 and end > 0:
            return domain + string[start+14:end]
        else:
            return None



