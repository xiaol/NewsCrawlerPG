# coding: utf-8

from functools import wraps
import logging

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






