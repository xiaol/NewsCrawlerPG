# coding: utf-8

import logging
from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, news_already_exists, g_cache_key
from News.utils.util import str_from_timestamp
from News.items import NewsItem, CommentItem
from News.constans.news163 import SPIDER_NAME
from News.constans.news163 import CRAWL_SOURCE
from News.constans.news163 import ARTICLE_URL_TEMPLATE
from News.constans.news163 import COMMENT_URL_TEMPLATE
from News.constans.news163 import DOMAIN
from News.extractor.news163 import News163Extractor

_logger = logging.getLogger(__name__)


class News163(NewsSpider):

    name = SPIDER_NAME
    default_comment_count = 30

    def g_news_meta_list(self, response):
        articles = load_json_data(response.body)
        if articles is None:
            _logger.error("spider has been banned for %s" % response.request.url)
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

        news["start_url"] = start_url
        news["start_meta_info"] = meta
        return news

    def g_news_request(self, item):
        url = self._g_article_url(item["docid"])
        return Request(
                url=url,
                callback=self.parse_news,
                meta={"news": item}
        )

    def parse_news(self, response):
        news = response.meta["news"]
        data = load_json_data(response.body)
        extractor = News163Extractor(data["content"], response.url, news=news)
        content, image_number = extractor.extract()
        news["content"] = content
        news["image_number"] = image_number
        if len(news["content"]) == 0:
            return
        else:
            yield news

    @staticmethod
    def _g_crawl_url(path):
        return DOMAIN + path

    @staticmethod
    def _g_article_url(docid):
        return ARTICLE_URL_TEMPLATE.format(docid=docid)

    def parse_comments(self, response):
        docid = response.meta["docid"]
        page = response.meta["page"]
        data = load_json_data(response.body)
        count = data["newListSize"]
        if count == 0: return
        comment_ids = data["commentIds"]
        comments = data["comments"]
        for comment_id in comment_ids:
            comment_id = comment_id.split(",")[-1]
            if comment_id in comments:
                item = self.g_comment_item(comments[comment_id], docid)
                if item is not None:
                    yield item
        if self.default_comment_count * page < count:
            yield self.g_comment_request(docid, page=page+1)

    def g_comment_item(self, comment, docid):
        item = CommentItem()
        item["docid"] = docid
        item["comment_id"] = comment["commentId"]
        item["content"] = comment["content"]
        user = comment["user"]
        item["nickname"] = user.get("nickname", "")
        item["profile"] = user.get("avatar", "")
        item["love"] = comment["vote"]
        item["create_time"] = comment["createTime"]
        if item["content"].strip():
            item["content"] = item["content"].strip().replace("<br>", "")
            return item
        else:
            return None

    def g_comment_request(self, docid, page=0):
        offset = page * self.default_comment_count
        url = self._g_comments_url(docid, offset)
        return Request(
            url=url,
            callback=self.parse_comments,
            meta={"docid": docid, "page": page}
        )

    @staticmethod
    def _g_comments_url(docid, offset):
        return COMMENT_URL_TEMPLATE.format(docid=docid, offset=offset)





