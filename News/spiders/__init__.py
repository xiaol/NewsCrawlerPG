# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from News.distributed import RedisSpider


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
