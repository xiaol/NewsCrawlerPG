# coding: utf-8

from News.constans.wechat import SPIDER_NAME
from News.constans.wechat import SOURCES
from News.utils.cache import Cache
from News.utils.util import get_query_from_url
from News.scheduler import g_queue_name
from News.scheduler import g_wechat_url


def start():
    c_key = g_queue_name(SPIDER_NAME)
    if Cache.llen(c_key) != 0:
        print("The previous task is not finished, please wait some time!")
        return
    for source in SOURCES:
        url = g_wechat_url(name=source["name"], oid=source["oid"])
        if not url:
            print("Can't get wexin sogou start url: %s" % source["name"])
            continue
        openid = get_query_from_url(url, "openid")
        if openid is None:
            print("Can't get openid for url: %s" % url)
            continue
        key = SPIDER_NAME + ":" + openid
        Cache.hmset(key, source)
        Cache.expire(key, 60*60*24)
        print("name: %s, oid: %s" % (source["name"], source["oid"]))
        print("start_url: %s\n" % url)
        Cache.lpush(c_key, url)

if __name__ == '__main__':
    start()

