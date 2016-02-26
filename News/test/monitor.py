# coding: utf-8

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
