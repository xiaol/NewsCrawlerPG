# coding: utf-8

from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.utils.util import str_from_timestamp
from News.items import get_default_news
from News.constans.toutiao import SPIDER_NAME
from News.constans.toutiao import DOMAIN
from News.constans.toutiao import CRAWL_SOURCE
from News.extractor import TouTiaoExtractor


class TouTiao(NewsSpider):

    name = SPIDER_NAME

    def parse(self, response):
        meta = response.meta.get("start_meta")
        data = load_json_data(response.body)
        articles = data.get("data", [])
        for article in articles:
            item = self.g_news_item(article, response.request.url, meta)
            if item is not None:
                yield self.g_news_request(item)

    def g_news_item(self, article, start_url="", meta=None):
        if article.get("has_video"):
            return None
        docid = article["source_url"]
        crawl_url = self._g_crawl_url(docid)
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            docid=docid,
            crawl_url=crawl_url,
            key=key,
            title=article["title"],
            tags=article.get("keywords", "").split(","),
            summary=article.get("abstract", ""),
            publish_time=str_from_timestamp(article["publish_time"]),
            love=article.get("favorite_count", 0),
            up=article.get("digg_count", 0),
            down=article.get("bury_count", 0),
            image_list=self._g_image_list(article),
            original_url=article.get("url", ""),
            original_source=article.get("source", ""),
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
        )
        if meta is not None:
            news["meta_channel_id"] = meta["channel"]
            news["meta_channel_name"] = meta["name"]
            news["meta_channel_online"] = meta["online"]
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
        body = response.body_as_unicode().encode("utf-8")
        extractor = TouTiaoExtractor(body)
        title, post_date, post_user, summary, content = extractor()
        news["content"] = content
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





