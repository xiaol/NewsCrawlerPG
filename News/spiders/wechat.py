# coding: utf-8

import logging
from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data
from News.items import NewsItem
from News.constans.wechat import SPIDER_NAME
from News.constans.wechat import CRAWL_SOURCE
from News.extractor.wechat import WechatExtractor

_logger = logging.getLogger(__name__)


class Wechat(NewsSpider):

    name = SPIDER_NAME
    custom_settings = {
        "DOWNLOAD_DELAY": 5,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.cookies.CookiesMiddleware": 700,
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "News.middlewares.RotateUserAgentMiddleware": None,
            "News.middlewares.WechatUserAgentMiddleware": 405,
        },
        "ITEM_PIPELINES": {
            "News.pipelines.CleanPipeline": 300,
            "News.pipelines.CompatiblePipeline": 301,
            "News.pipelines.CachePipeline": 302,
            "News.pipelines.MongoPipeline": 303,
        },
    }

    def parse(self, response):
        results = load_json_data(response.body)
        if results is None:
            _logger.error("spider has been banned for %s" % response.request.url)
            return
        total = int(results["totalPages"])
        page = int(results["page"])
        articles = results["items"]
        for article in articles:
            item = self.g_news_item(article, response.request.url)
            if item is not None:
                request = self.g_news_request(item)
                request.meta["browser"] = response.meta["browser"]
                yield request

    def g_news_item(self, article, start_url=""):
        news = NewsItem()
        news["docid"] = ""
        crawl_url = self._g_crawl_url(article)
        if not crawl_url: return None
        news["crawl_url"] = crawl_url
        news["key"] = self.g_cache_key(crawl_url)
        if self.news_already_exists(news["key"]): return None
        news["title"] = ""
        news["tags"] = list()
        news["summary"] = self._g_crawl_summary(article)
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
        news = response.meta["news"]
        redirects = response.request.meta.get("redirect_urls")
        if redirects:
            news["crawl_url"] = response.url
            news["key"] = self.g_cache_key(news["crawl_url"])
        extractor = WechatExtractor(response.body, response.url,
                                    hard_tags=[], news=news)
        content, image_number = extractor.extract()
        news["content"] = content
        news["image_number"] = image_number
        yield news

    @staticmethod
    def _g_crawl_url(string):
        domain = "http://weixin.sogou.com"
        start = string.find("<url><![CDATA[")
        end = string.find("]]></url>")
        if start > 0 and end > 0:
            return domain + string[start+14:end]
        else:
            return None

    @staticmethod
    def _g_crawl_summary(string):
        start = string.find("<content><![CDATA[")
        end = string.find("]]></content>")
        if start > 0 and end > 0:
            return string[start+18:end]
        else:
            return ""



