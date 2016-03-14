import json
from urlparse import urlparse, parse_qs
from time import strftime, localtime
import base64
from News.utils.cache import Cache


def load_json_data(data):
    try:
        d = json.loads(data)
    except:
        return None
    else:
        return d


def str_from_timestamp(timestap):
    time_format = "%Y-%m-%d %H:%M:%S"
    return strftime(time_format, localtime(timestap))


def get_query_from_url(url, key):
    string = urlparse(url).query
    params = parse_qs(qs=string)
    values = params.get(key, [])
    if len(values) != 1:
        return None
    else:
        return values[0]


def news_already_exists(key):
    boolean = Cache.exist(key)
    return boolean


def g_cache_key(string):
    return "news:" + base64.urlsafe_b64encode(string).replace("=", "")

if __name__ == '__main__':
    print get_query_from_url("http://weixin.sogou.com/gzh?openid=oIWsFt_60J20VTUbAEOviZNWlmcQ&ext=YKOZhC_DksAQw_O0t2RIJkqANb8zNrvTCpxMre_VM43JSuDjdCJr4Xy4Zg6Cb4T1", "oopenid")




