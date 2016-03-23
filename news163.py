# coding: utf-8
import types
from News.constans.news163 import SPIDER_NAME
from News.constans.news163 import CHANNELS, CITIES
from News.utils.cache import Cache
from News.scheduler import g_queue_name
from News.scheduler import g_news163_urls, g_news163_local_urls


def start():
    key = g_queue_name(SPIDER_NAME)
    channels = {}
    urls = list()
    # for key, value in CHANNELS.items():
    #     if isinstance(value["channel"], types.IntType):
    #         channels[key] = value
    # urls = g_news163_urls(channels=channels, offset=0, end=100)
    cities = "北京"   # CITIES
    local_urls = g_news163_local_urls(cities=cities, offset=0, end=100)
    urls.extend(local_urls)
    if Cache.llen(key) != 0:
        print("the last task is not processed, please wait some time!")
    else:
        Cache.lpush(key, *urls)


if __name__ == '__main__':
    start()

