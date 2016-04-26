# coding: utf-8

from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.items import get_default_news
from News.constans.yidianzixun import SPIDER_NAME
from News.constans.yidianzixun import COMMENT_SPIDER_NAME
from News.constans.yidianzixun import ARTICLE_URL_TEMPLATE
from News.constans.yidianzixun import CRAWL_SOURCE
from News.extractor import YiDianZiXunExtractor


class YiDianZiXun(NewsSpider):

    name = SPIDER_NAME

    def g_news_meta_list(self, response):
        data = load_json_data(response.body)
        if data is not None:
            return data.get("result", [])
        else:
            self.logger.warning("can't get data")

    def g_news_item(self, article, start_url="", meta=None):
        if article["ctype"] not in ["news", "picture"]:
            return None  # fixme: only support news now
        docid = article["docid"]
        crawl_url = self._g_article_url(article.get("url"), docid)
        if not crawl_url:
            return None
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
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
            comment_url=self._g_comment_url(docid),
            comment_queue=COMMENT_SPIDER_NAME+":start_urls"
        )
        news["docid"] = news["comment_url"]
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
            extractor = YiDianZiXunExtractor(body, response.url)
            title, post_date, post_user, summary, content = extractor()
            news["content"] = content
            news["content_html"] = response.body
            yield news

    def _g_article_url(self, url, docid):
        if not url or url.startswith("http://www.yidianzixun.com"):
            return ARTICLE_URL_TEMPLATE.format(docid=docid)
        else:
            self.logger.warning("outer link: %s" % url)
            return ""

    @staticmethod
    def _g_comment_url(docid):
        template = "http://www.yidianzixun.com/api/q/?path=contents/comments&count=100&docid={docid}"
        return template.format(docid=docid)

