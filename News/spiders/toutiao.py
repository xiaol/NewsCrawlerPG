# coding: utf-8

from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.utils.util import str_from_timestamp
from News.items import get_default_news
from News.constans.toutiao import SPIDER_NAME
from News.constans.toutiao import COMMENT_SPIDER_NAME
from News.constans.toutiao import DOMAIN
from News.constans.toutiao import CRAWL_SOURCE
from News.extractor import TouTiaoExtractor
from newsextractor import extract


class TouTiao(NewsSpider):

    name = SPIDER_NAME

    def g_news_meta_list(self, response):
        data = load_json_data(response.body)
        if data is not None:
            return data.get("data", [])
        else:
            self.logger.warning("can't get data: url: %s body: %s" % (response.url, response.body_as_unicode()))
            return []

    def g_news_item(self, article, start_url="", meta=None):
        if article.get("has_video"):
            return None
        docid = article["source_url"]
        crawl_url = self._g_crawl_url(article)
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            crawl_url=crawl_url,
            key=key,
            title=article["title"],
            tags=article.get("keywords", "").split(","),
            summary=article.get("abstract", ""),
            publish_time=str_from_timestamp(article["publish_time"]),
            love=article.get("favorite_count", 0),
            up=article.get("digg_count", 0),
            down=article.get("bury_count", 0),
            original_url=article.get("url", ""),
            original_source=article.get("source", ""),
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
            start_meta_info=meta,
            comment_url=self._g_comment_url(docid),
            comment_queue=COMMENT_SPIDER_NAME+":start_urls"
        )
        news["docid"] = news["comment_url"]
        return news

    def parse_news(self, response):
        news = response.meta["news"]
        redirects = response.request.meta.get("redirect_urls")
        if redirects:
            news["crawl_url"] = response.url
        body = response.body_as_unicode().encode("utf-8")
        if news["crawl_url"].startswith(DOMAIN):
            extractor = TouTiaoExtractor(body, news["crawl_url"])
            title, post_date, post_user, summary, content = extractor()
        else:
            try:
                title, post_date, post_user, summary, tags, content = extract(news["crawl_url"], document=body)
            except Exception as e:
                self.logger.warning(e.message + " outer link: %s" % news["crawl_url"])
                return
        if content:
            news["content"] = content
            news["content_html"] = response.body
            yield news
        else:
            self.logger.warning("content empty: %s" % news["crawl_url"])

    def _g_crawl_url(self, article):
        return DOMAIN + article["source_url"]

    @staticmethod
    def _g_comment_url(docid):
        template = "http://toutiao.com{docid}comments/?count=100&offset=0&format=json"
        comment_url = template.format(docid=docid)
        return comment_url




