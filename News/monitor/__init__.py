# coding: utf-8

from datetime import datetime
from functools import wraps
import logging

from News.utils.cache import Cache

_logger = logging.getLogger(__name__)


def _record_error_log(item, error):
    _logger.error("\ncrawl_url:%s\n"
                  "original_url:%s\n"
                  "crawl_source:%s\n"
                  "original_source:%s\n"
                  "channel:%s\n"
                  "error:%s" % (
                    item["crawl_url"],
                    item["original_url"],
                    item["crawl_source"],
                    item["original_source"],
                    item["channel"],
                    error)
                  )


def monitor(error):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            content, count = func(self, *args, **kwargs)
            if len(content) == 0 and error in [1, 2]:
                _record_error_log(self.news, error)
            return content, count
        return wrapper
    return decorator


def redis_monitor_news(key, value):
    Cache.lpush(key, value)
    Cache.expire(key, 1296000)  # 60*60*24*15


def _get_today_string():
    now = datetime.now()
    return now.strftime("%Y%m%d")


def monitor_news_in_pipeline(sid):
    tail = _get_today_string()
    key = "spider:news:monitor:pipeline:" + tail
    redis_monitor_news(key, value=sid)


def monitor_news_store_success(sid):
    tail = _get_today_string()
    key = "spider:news:monitor:store:success:" + tail
    redis_monitor_news(key, value=sid)



