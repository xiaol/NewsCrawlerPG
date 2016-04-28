# coding: utf-8

from News.constans import CHANNELS_MAP

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-27 18:28"


def g_spider_source(categories, source_name):
    sources = []
    if isinstance(categories, list):
        _g_special_spider_source(categories, sources)
    elif isinstance(categories, dict):
        _g_spider_source(categories, source_name, sources)
    else:
        pass
    return sources


def _g_special_spider_source(categories, sources):
    for item in categories:
        source = dict()
        oid = item["oid"]
        name = item["name"]
        source_name = name + ";" + oid
        channel_id = item["channel_id"]
        channel = CHANNELS_MAP[channel_id]
        channel_name = channel["name"]
        channel_status = channel["online"]

        source["source_url"] = item["url"]
        source["source_name"] = source_name
        source["channel_name"] = channel_name
        source["channel_id"] = channel_id
        source["descr"] = item["description"]
        source["frequency"] = item["frequency"]
        source["status"] = channel_status
        sources.append(source)


def _g_spider_source(categories, source_name, sources, prefix=""):
    for k, v in categories.items():
        if isinstance(v, dict):
            _g_spider_source(v, source_name, sources, prefix=prefix+k+"/")
        elif isinstance(v, tuple):
            if v[1] is None:
                continue
            source = dict()
            url = v[0]
            channel_id = v[1]
            channel = CHANNELS_MAP[channel_id]
            channel_name = channel["name"]
            channel_status = channel["online"]
            frequency = v[2]
            descr = prefix + k

            source["source_url"] = url
            source["source_name"] = source_name
            source["channel_name"] = channel_name
            source["channel_id"] = channel_id
            source["descr"] = descr
            source["frequency"] = frequency
            source["status"] = channel_status
            sources.append(source)
        else:
            raise ValueError("wrong format")





