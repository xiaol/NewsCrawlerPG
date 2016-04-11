# coding: utf-8

"""
爬虫按频率调度
"""

from importlib import import_module
import time
from News.constans import SPIDER_CONFIG_NAMES
from News.scheduler import g_start_request, g_queue_name
from News.utils.cache import Cache

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-07 12:00"


def g_start_urls(categories, spider_name, scheduler_list):
    for k, v in categories.items():
        if isinstance(v, dict):
            g_start_urls(v, spider_name, scheduler_list)
        elif isinstance(v, tuple):
            if v[1] is None:
                continue
            url = v[0]
            value = {"channel": v[1]}
            interval = 60*60 if len(v) < 3 else v[2]*60
            request = g_start_request(url, value)
            start_schedule_time = int(time.time())
            queue = g_queue_name(spider_name)
            info = {
                "time": start_schedule_time,
                "interval": interval,
                "request": request,
                "queue": queue,
            }
            scheduler_list.append(info)
        else:
            raise Exception


def g_all_scheduler_info():
    scheduler_list = list()
    for name in SPIDER_CONFIG_NAMES:
        cfg = import_module(name=name)
        g_start_urls(cfg.CATEGORIES, cfg.SPIDER_NAME, scheduler_list)
    return scheduler_list


def push_request_to_queue(queue, request):
    Cache.lpush(queue, request)


def run():
    scheduler_info_list = g_all_scheduler_info()
    while 1:
        for index, info in enumerate(scheduler_info_list):
            now = int(time.time())
            last = info["time"]
            interval = info["interval"]
            request = info["request"]
            queue = info["queue"]
            if now >= last + interval:
                push_request_to_queue(queue, request)
                scheduler_info_list[index]["time"] = now
        time.sleep(30)


if __name__ == '__main__':
    run()




