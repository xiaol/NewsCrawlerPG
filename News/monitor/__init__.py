# coding: utf-8

from functools import wraps

from News.database import Monitor
from News.database import session


def _record_error_log(item, error):
    m = Monitor(
        crawl_url=item["crawl_url"],
        original_url=item["original_url"],
        crawl_source=item["crawl_source"],
        original_source=item["original_source"],
        channel=item["channel"],
        error=error,
    )
    try:
        session.add(m)
        session.commit()
    except Exception as e:
        session.rollback()


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






