# coding: utf-8

from urllib import urlencode

from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.items import get_default_news
from News.constans.yidianzixun import SPIDER_NAME
from News.constans.yidianzixun import ARTICLE_URL_TEMPLATE
from News.constans.yidianzixun import CRAWL_SOURCE
from News.extractor import YiDianZiXunExtractor


class YiDianZiXun(NewsSpider):

    name = SPIDER_NAME

    def g_news_meta_list(self, response):
        data = load_json_data(response.body)
        return data.get("result", [])

    def g_news_item(self, article, start_url="", meta=None):
        if article["ctype"] != "news":
            return None  # fixme: only support news now
        docid = article["docid"]
        crawl_url = self._g_article_url(docid)
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            docid=docid,
            crawl_url=crawl_url,
            key=key,
            title=article["title"],
            summary=article.get("summary", ""),
            publish_time=article["date"],
            love=article.get("like", 0),
            up=article.get("up", 0),
            original_url=article.get("url", ""),
            crawl_source=CRAWL_SOURCE,
            original_source=article.get("source", ""),
            start_url=start_url,
            start_meta_info=meta,
        )
        return news

    def parse_news(self, response):
        news = response.meta["news"]
        if "window.location.replace" in response.body:
            news["crawl_url"] = news["original_url"]
            news["key"] = g_cache_key(news["crawl_url"])
            yield self.g_news_request(news)
        else:
            redirects = response.request.meta.get("redirect_urls")
            if redirects:
                news["crawl_url"] = response.url
                news["key"] = g_cache_key(news["crawl_url"])
            body = response.body_as_unicode().encode("utf-8")
            extractor = YiDianZiXunExtractor(body)
            title, post_date, post_user, summary, content = extractor()
            news["content"] = content
            yield news

    @staticmethod
    def _g_article_url(docid):
        return ARTICLE_URL_TEMPLATE.format(docid=docid)

    @staticmethod
    def _g_image_url(url, news_id):
        _image = "http://i1.go2yd.com/image.php?"
        params = {
            "url": url,
            "news_id": news_id,
            "type": "thumbnail_192x108"
        }
        return _image + urlencode(params)




