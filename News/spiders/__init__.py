# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import base64
import logging

from scrapy_redis.spiders import RedisSpider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
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
    def get_img_number(content):
        pass


class GeneralSpider(CrawlSpider):

    name = "general"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = ["http://news.sina.com.cn"]
    rules = (
        Rule(LinkExtractor(allow=("http://news.sina.com.cn/[a-z]/[a-z]{2}/\d{4}-\d{2}-\d{2}/.*\.shtml", )), callback="parse_item", ),
    )

    def parse_item(self, response):
        print response.url





