# coding: utf-8

from News.constans.wechat import SPIDER_NAME
from News.utils.cache import Cache
from News.scheduler import g_queue_name
from News.scheduler import g_wechat_url


def start():
    name = u"外媒看天朝"
    oid = "iwaimei"
    key = g_queue_name(SPIDER_NAME)
    url = g_wechat_url(name=name, oid=oid)
    if not url:
        print("can't get wexin sogou start url: %s" % name)
    else:
        print("start_url: %s" % url)
        if Cache.llen(key) != 0:
            print("the last task is not processed, please wait some time!")
        else:
            Cache.lpush(key, url)

if __name__ == '__main__':
    start()

