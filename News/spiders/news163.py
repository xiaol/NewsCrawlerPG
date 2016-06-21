# coding: utf-8

from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, news_already_exists, g_cache_key
from News.utils.util import str_from_timestamp
from News.items import NewsItem
from News.constans.news163 import SPIDER_NAME
from News.constans.news163 import COMMENT_SPIDER_NAME
from News.constans.news163 import CRAWL_SOURCE
from News.constans.news163 import ARTICLE_URL_TEMPLATE
from News.constans.news163 import COMMENT_URL_TEMPLATE
from News.constans.news163 import DOMAIN
from News.extractor import News163Extractor


class News163(NewsSpider):

    name = SPIDER_NAME
    default_comment_count = 30

    def g_news_meta_list(self, response):
        articles = load_json_data(response.body)
        if articles is None:
            self.logger.error("spider has been banned for %s" % response.request.url)
            return []
        else:
            return articles

    def g_news_item(self, article, start_url="", meta=None):
        news = NewsItem()
        news["docid"] = article["docID"]
        url_163 = article.get("url_163", None)
        if url_163 is None: return None
        news["crawl_url"] = self._g_crawl_url(url_163)
        news["key"] = g_cache_key(news["crawl_url"])
        if news_already_exists(news["key"]): return None
        news["title"] = article["title"]
        news["tags"] = list()
        news["summary"] = article["summary"]
        news["publish_time"] = str_from_timestamp(article["publish_time"]/1000)
        news["content"] = list()
        position = article.get("position", "null,null,null,null").split(",")
        news["province"] = position[0] if position[0] != "null" else None
        news["city"] = position[1] if position[1] != "null" else None
        news["district"] = position[2] if position[2] != "null" else None
        news["love"] = 0
        news["up"] = 0
        news["down"] = 0

        news["original_url"] = article.get("doc_url", "")
        news["channel"] = article.get("channel", "/").split("/")[0]
        news["category"] = article.get("category", "")
        news["crawl_source"] = CRAWL_SOURCE
        news["original_source"] = article.get("source", "")
        if news['original_source'] == '糗事百科':
            return None

        news["comment_url"] = self._g_comment_url(docid=news["docid"])
        news["comment_queue"] = COMMENT_SPIDER_NAME + ":start_urls"
        news["start_url"] = start_url
        news["start_meta_info"] = meta
        return news

    def g_news_request(self, item):
        url = self._g_article_url(item["docid"])
        item["docid"] = item["comment_url"]
        return Request(
                url=url,
                callback=self.parse_news,
                meta={"news": item}
        )

    def parse_news(self, response):
        news = response.meta["news"]
        data = load_json_data(response.body)
        if data and data.get("content"):
            body = '<div id="inner_article">' + data["content"] + "</div>"
            extractor = News163Extractor(body)
            title, post_date, post_user, summary, content = extractor()
            news["content"] = content
            news["content_html"] = body
            if len(news["content"]) == 0:
                return
            else:
                yield news
        else:
            self.logger.warning("can't get content url: %s body: %s" % (response.url, response.body_as_unicode()))

    @staticmethod
    def _g_crawl_url(path):
        return DOMAIN + path

    @staticmethod
    def _g_article_url(docid):
        return ARTICLE_URL_TEMPLATE.format(docid=docid)

    @staticmethod
    def _g_comment_url(docid, offset=0, count_per_page=30):
        return COMMENT_URL_TEMPLATE.format(docid=docid, offset=offset,
                                           count_per_page=count_per_page)





