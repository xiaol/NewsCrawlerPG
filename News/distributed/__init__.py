# coding: utf-8

import json
import logging

from scrapy.http import Request
from scrapy_redis.spiders import RedisSpider

_logger = logging.getLogger(__name__)


class RedisMetaSpider(RedisSpider):
    """ 带 meta 信息的 RedisSpider

        接收 json 信息，格式为 {"id": 1, "url": "", "meta": {}}，子类在 response 中
        可直接取出 meta，子类可重写 g_url_from_config, g_meta_from_config 来生成需要
        的信息
    """

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
                assert isinstance(config, dict)
                sid = config.get("id")
                config["meta"]["monitor_id"] = sid
                url = self.g_url_from_config(config)
                meta = self.g_meta_from_config(config)
                if url:
                    return self.make_requests_from_url_meta(url, meta)
                else:
                    _logger.error("generate start url error")

    def g_url_from_config(self, config):
        return config["url"]

    def g_meta_from_config(self, config):
        return config["meta"]
