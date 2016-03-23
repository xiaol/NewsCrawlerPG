# coding: utf-8

import json

from scrapy import Spider, signals
from scrapy.http import Request
from scrapy.exceptions import DontCloseSpider

import redis


# Default values.
REDIS_URL = None
REDIS_HOST = 'localhost'
REDIS_PORT = 6379


def from_settings(settings):
    url = settings.get('REDIS_URL',  REDIS_URL)
    host = settings.get('REDIS_HOST', REDIS_HOST)
    port = settings.get('REDIS_PORT', REDIS_PORT)

    # REDIS_URL takes precedence over host/port specification.
    if url:
        return redis.from_url(url)
    else:
        return redis.Redis(host=host, port=port)


class RedisMixin(object):
    """Mixin class to implement reading urls from a redis queue."""
    redis_key = None  # use default '<spider>:start_urls'

    def setup_redis(self):
        """Setup redis connection and idle signal.

        This should be called after the spider has set its crawler object.
        """
        if not self.redis_key:
            self.redis_key = '%s:start_urls' % self.name

        self.server = from_settings(self.crawler.settings)
        # idle signal is called when the spider has no requests left,
        # that's when we will schedule new requests from redis queue
        self.crawler.signals.connect(self.spider_idle, signal=signals.spider_idle)
        self.crawler.signals.connect(self.item_scraped, signal=signals.item_scraped)
        self.log("Reading URLs from redis list '%s'" % self.redis_key)

    def make_requests_from_url_meta(self, url, meta=None):
        return Request(url, dont_filter=True, meta={"start_meta": meta})

    def next_request(self):
        """Returns a request to be scheduled or none."""
        config = self.server.lpop(self.redis_key)
        if config:
            try:
                config = json.loads(config)
            except Exception:
                self.log("json load error from %s" % self.redis_key)
            else:
                url = config["url"]
                meta = config["meta"]
                if url:
                    return self.make_requests_from_url_meta(url, meta)

    def schedule_next_request(self):
        """Schedules a request if available"""
        req = self.next_request()
        if req:
            self.crawler.engine.crawl(req, spider=self)

    def spider_idle(self):
        """Schedules a request if available, otherwise waits."""
        self.schedule_next_request()
        raise DontCloseSpider

    def item_scraped(self, *args, **kwargs):
        """Avoids waiting for the spider to  idle before scheduling the next request"""
        self.schedule_next_request()


class RedisSpider(RedisMixin, Spider):
    """Spider that reads urls from redis queue when idle."""

    def _set_crawler(self, crawler):
        super(RedisSpider, self)._set_crawler(crawler)
        self.setup_redis()
