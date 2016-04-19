# coding: utf-8

import logging
from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.items import get_default_news
from News.constans.wechat import SPIDER_NAME
from News.constans.wechat import CRAWL_SOURCE
from News.extractor import WechatExtractor
from News.scheduler import wechat

_logger = logging.getLogger(__name__)


class Wechat(NewsSpider):

    name = SPIDER_NAME
    custom_settings = {
        "DOWNLOAD_DELAY": 10,
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
            # "News.pipelines.PrintPipeline": 304,
        },
    }

    def g_url_from_config(self, config):
        meta = config["meta"]
        source_name = meta["source_name"].split(";")
        name = source_name[0]
        oid = source_name[1]
        return wechat.get_start_url(name, oid)

    def g_news_meta_list(self, response):
        results = load_json_data(response.body)
        if results is None:
            _logger.error("spider has been banned for %s" % response.request.url)
            return []
        else:
            return results["items"]

    def g_news_item(self, article, start_url="", meta=None):
        crawl_url = self._g_crawl_url(article)
        if not crawl_url: return None
        news = get_default_news(
            crawl_url=crawl_url,
            key=g_cache_key(crawl_url),
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
            summary=self._g_crawl_summary(article),
            start_meta_info=meta,
        )
        return None if news_already_exists(news["key"]) else news

    def parse_news(self, response):
        news = response.meta["news"]
        redirects = response.request.meta.get("redirect_urls")
        if redirects:
            news["crawl_url"] = response.url
            news["key"] = g_cache_key(news["crawl_url"])
        body = response.body_as_unicode().encode("utf-8")
        extractor = WechatExtractor(body, response.url)
        title, post_date, post_user, summary, content = extractor()
        news["title"] = title
        news["publish_time"] = post_date
        news["original_source"] = post_user
        news["original_url"] = news["crawl_url"]
        news["content"] = content
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



