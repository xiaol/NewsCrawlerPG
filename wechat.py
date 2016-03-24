# coding: utf-8

import random
import time

from News.constans.wechat import SPIDER_NAME
from News.constans.wechat import SOURCES
from News.utils.cache import Cache
from News.scheduler import g_queue_name
from News.scheduler import g_wechat_urls


def start():
    key = g_queue_name(SPIDER_NAME)
    if Cache.llen(key) != 0:
        print("The previous task is not finished, please wait some time!")
        return
    sources = SOURCES
    urls = g_wechat_urls(sources)
    for i, url in enumerate(urls):
        if i > 0:
            time.sleep(random.randint(60, 180))
        Cache.lpush(key, url)


if __name__ == '__main__':
    start()

