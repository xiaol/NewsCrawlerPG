# coding: utf-8

from News.constans.news163 import SPIDER_NAME
from News.constans.news163 import CHANNELS
from News.utils.cache import Cache
from News.scheduler import g_queue_name
from News.scheduler import g_news163_urls


def start():
    channel_keys = ["娱乐", "体育", "科技", "搞笑", "财经", "汽车", "游戏", "历史",
                    "美女", "旅游", "美食", "养生"]
    key = g_queue_name(SPIDER_NAME)
    channels = {}
    for channel in CHANNELS:
        if channel in channel_keys:
            channels[channel] = CHANNELS[channel]
    urls = g_news163_urls(channels=channels, offset=0, end=100, cities="北京")  # cities="北京"
    if Cache.llen(key) != 0:
        print("the last task is not processed, please wait some time!")
    else:
        Cache.lpush(key, *urls)


if __name__ == '__main__':
    start()

