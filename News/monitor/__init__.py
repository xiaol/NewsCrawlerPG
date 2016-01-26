# coding: utf-8

from functools import wraps

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
POSTGRES = "postgresql://postgres:lee@localhost/test"
Base = automap_base()
engine = create_engine(POSTGRES)
Base.prepare(engine, reflect=True)
# News = Base.classes.newslist
# Comments = Base.classes.newscomments
Monitor = Base.classes.monitor
session = Session(engine)


def _record_error_log(item, error):
    m = Monitor(
        crawl_url=item["crawl_url"],
        original_url=item["original_url"],
        crawl_source=item["crawl_source"],
        original_source=item["original_source"],
        channel="news",
        error=error,
    )
    session.add(m)
    session.commit()


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






