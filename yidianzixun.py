# coding: utf-8

from News.constans.yidianzixun import SPIDER_NAME
from News.constans.yidianzixun import CHANNELS
from News.utils.cache import Cache
from News.scheduler import g_queue_name
from News.scheduler import g_yidianzixun_urls


def start():
    key = g_queue_name(SPIDER_NAME)
    urls = g_yidianzixun_urls(channels=CHANNELS)
    if Cache.llen(key) != 0:
        print("the last task is not processed, please wait some time!")
    else:
        Cache.lpush(key, *urls)


if __name__ == '__main__':
    start()


