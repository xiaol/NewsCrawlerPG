# coding: utf-8

from News.constans.jandan_net import CATEGORIES, SPIDER_NAME
from News.scheduler import g_category_two_urls, g_queue_name
from News.utils.cache import Cache

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-29 17:24"


def start():
    key = g_queue_name(SPIDER_NAME)
    sources = CATEGORIES
    urls = g_category_two_urls(sources)
    if Cache.llen(key) != 0:
        print("the last task is not processed, please wait some time!")
    else:
        Cache.lpush(key, *urls)


if __name__ == '__main__':
    start()