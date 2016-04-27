# coding: utf-8

from importlib import import_module
from News.scheduler.sources import g_spider_source
from News.scheduler import g_queue_name

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-27 18:43"


def main():
    path = raw_input("please input spider config path: ").strip()
    cfg = import_module(path)
    spider_name = cfg.SPIDER_NAME
    categories = cfg.CATEGORIES
    source_name = cfg.CRAWL_SOURCE
    spider_queue_name = g_queue_name(spider_name)
    sources = g_spider_source(categories, source_name)
    saves = []
    for index, source in enumerate(sources):
        source["queue_name"] = spider_queue_name
        save = (
            index,
            source["channel_name"],
            source["channel_id"],
            source["source_name"],
            source["queue_name"],
            source["frequency"],
            source["source_url"],
        )
        saves.append(save)
    with open("db_spider_sources.py", "w+") as f:
        f.write("SOURCE = " + saves.__repr__())


if __name__ == '__main__':
    main()
