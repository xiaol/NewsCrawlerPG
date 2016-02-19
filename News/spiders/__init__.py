# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import base64
import logging

from scrapy_redis.spiders import RedisSpider
from News.utils.cache import Cache

_logger = logging.getLogger(__name__)


class NewsSpider(RedisSpider):

    def parse(self, response):
        raise NotImplementedError

    def g_news_item(self, item):
        raise NotImplementedError

    def g_news_request(self, item):
        raise NotImplementedError

    def parse_news(self, response):
        raise NotImplementedError

    @staticmethod
    def news_already_exists(key):
        boolean = Cache.exist(key)
        if boolean:
            _logger.info("cache exists: %s" % key)
        return boolean

    @staticmethod
    def g_cache_key(string):
        return "news:" + base64.urlsafe_b64encode(string).replace("=", "")
