# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import abc
import six
from scrapy import Request, Spider
from News.distributed import RedisSpider


@six.add_metaclass(abc.ABCMeta)
class NewsSpider(RedisSpider):

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



