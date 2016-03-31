# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import abc
import six
from importlib import import_module
from urlparse import urljoin
import logging
from scrapy import Request, Spider
from News.distributed import RedisSpider
from News.items import get_default_news
from News.utils.util import g_cache_key, news_already_exists, load_json_data
from News.extractor import GeneralExtractor

_logger = logging.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class NewsSpider(Spider):

    def parse(self, response):
        """
        """
        meta = response.meta.get("start_meta")
        articles = self.g_news_meta_list(response)
        for article in articles:
            item = self.g_news_item(article, response.request.url, meta)
            if item is not None:
                yield self.g_news_request(item)

    @abc.abstractmethod
    def g_news_meta_list(self, response):
        """
        """

    @abc.abstractmethod
    def g_news_item(self, article, start_url="", meta=None):
        """
        """

    def g_news_request(self, item):
        """
        """
        return Request(
            url=item["crawl_url"],
            callback=self.parse_news,
            meta={"news": item}
        )

    @abc.abstractmethod
    def parse_news(self, response):
        """
        """


class ConfigNewsSpider(NewsSpider):
    """
    """

    def g_news_meta_list(self, response):
        if hasattr(self, "ajax"):
            if self.ajax:
                return self.g_ajax_news_meta_list(response)
            else:
                return self.g_normal_news_meta_list(response)
        else:
            return self.g_normal_news_meta_list(response)

    def g_normal_news_meta_list(self, response):
        base = response.url
        items = response.xpath(self.items_xpath)
        _logger.info("items len: %s" % len(items))
        articles = list()
        for item in items:
            article = dict()
            title = item.xpath(self.title_xpath).extract()
            url = item.xpath(self.url_xpath).extract()
            if hasattr(self, "summary_xpath"):
                summary = item.xpath(self.summary_xpath).extract()
                if summary:
                    article["summary"] = summary[0]
            if hasattr(self, "thumb_xpath"):
                thumb = item.xpath(self.thumb_xpath).extract()
                if thumb:
                    article["thumb"] = urljoin(base, thumb[0])
            if title and url:
                article["title"] = title[0]
                article["url"] = urljoin(base, url[0])
                articles.append(article)
            else:
                _logger.warn("title: %s, url: %s" % ("".join(title), "".join(url)))
        return articles

    def g_ajax_news_meta_list(self, response):
        body = load_json_data(response.body_as_unicode())
        items = self.get_dict_value(body, self.items_xpath)
        _logger.info("item len: %s" % len(items))
        articles = list()
        for item in items:
            article = dict()
            article["title"] = self.get_dict_value(item, self.title_xpath)
            article["url"] = self.get_dict_value(item, self.url_xpath)
            if hasattr(self, "summary_xpath"):
                article["summary"] = self.get_dict_value(item, self.summary_xpath)
            if hasattr(self, "thumb_xpath"):
                article["thumb"] = self.get_dict_value(item, self.thumb_xpath)
            articles.append(article)
        return articles

    @staticmethod
    def get_dict_value(d, path):
        value = d
        for key in path.split("|"):
            value = value[key]
        return value

    def g_news_item(self, article, start_url="", meta=None):
        crawl_url = article["url"]
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            title=article["title"],
            crawl_url=crawl_url,
            docid=crawl_url,
            key=key,
            crawl_source=self.crawl_source,
            start_url=start_url,
            summary=article.get("summary", "")
        )
        if meta is not None:
            news["meta_channel_id"] = meta["channel"]
            news["meta_channel_name"] = meta["name"]
            news["meta_channel_online"] = meta["online"]
        return news

    def parse_news(self, response):
        news = response.meta["news"]
        body = response.body_as_unicode().encode("utf-8")
        title_param = self.title_param if hasattr(self, "title_param") else None
        post_date_param = self.post_date_param if hasattr(self, "post_date_param") else None
        post_user_param = self.post_user_param if hasattr(self, "post_user_param") else None
        summary_param = self.summary_param if hasattr(self, "summary_param") else None
        content_param = self.content_param if hasattr(self, "content_param") else None
        if hasattr(self, "extractor_cls"):
            extractor_cls = import_module(name=self.extractor_cls)
        else:
            extractor_cls = GeneralExtractor
        extractor = extractor_cls(body)
        title, post_date, post_user, summary, content = extractor(
            title_param=title_param,
            post_date_param=post_date_param,
            post_user_param=post_user_param,
            summary_param=summary_param,
            content_param=content_param,
        )
        news["publish_time"] = post_date
        news["content"] = content
        yield news




