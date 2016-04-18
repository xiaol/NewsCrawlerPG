# coding: utf-8

import json

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider


class RedisMetaSpider(RedisSpider):

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


