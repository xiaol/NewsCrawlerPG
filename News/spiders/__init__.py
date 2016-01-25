# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import base64
from scrapy_redis.spiders import RedisSpider
from News.utils.cache import Cache


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
        return Cache.exist(key)

    @staticmethod
    def g_cache_key(string):
        return "news:" + base64.encodestring(string).replace("=", "")
