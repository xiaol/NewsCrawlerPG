# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import logging

import requests
from scrapy.exceptions import DropItem

from News.constans import CACHE_SOURCE_KEY
from News.constans import NEWS_STORE_API
from News.constans import COMMENT_STORE_API
from News.utils.cache import Cache
from News.items import NewsItem, CommentItem

_logger = logging.getLogger(__name__)


class NewsPipeline(object):

    def __init__(self):
        cache_source_key = CACHE_SOURCE_KEY
        self.sources = self.get_cache_sources(cache_source_key)

    @staticmethod
    def get_cache_sources(cache_source_key):
        """ local cache source info in redis """
        sources = Cache.hgetall(cache_source_key)
        for k, v in sources.iteritems():
            sources[k] = json.loads(v)
        return sources

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            _logger.info("title: %s" % item["title"])
            if len(item["content"]) == 0:
                raise DropItem("content empty: %s" % item["crawl_url"])
            else:
                self.cache_news(item)
                self.store_news(item)
        elif isinstance(item, CommentItem):
            pass
            # self.store_comment(item)
        return item

    def cache_news(self, item):
        obj = dict()
        obj["key"] = item["key"]
        obj["url"] = item["crawl_url"]
        obj["docid"] = item["docid"]
        obj["title"] = item["title"]
        obj["keywords"] = ",".join(item["tags"])
        obj["synopsis"] = item["summary"]
        obj["love"] = item["love"]
        obj["up"] = item["up"]
        obj["author"] = ""
        obj["pub_url"] = item["original_url"]
        obj["pub_name"] = item["original_source"]
        obj["pub_time"] = item["publish_time"]
        obj["img_num"] = item["image_number"]
        obj["img_list"] = json.dumps([])
        obj["content"] = json.dumps(item["content"])
        obj["content_html"] = ""
        if item.get("province"):
            obj["province"] = item["province"]
        if item.get("city"):
            obj["city"] = item["city"]
        if item.get("district"):
            obj["district"] = item["district"]

        start_url = item["start_url"]
        if start_url in self.sources:
            source = self.sources[start_url]
            obj["source_id"] = source["id"]
            obj["source_name"] = source["sourceName"]
            obj["channel_name"] = source["channelName"]
            obj["channel_id"] = source["channelId"]
            obj["source_online"] = source["online"]
            Cache.hmset(item["key"], obj)
        else:
            raise DropItem("no spider info, start_url:%s" % start_url)

    @staticmethod
    def store_news(item):
        url = NEWS_STORE_API.format(key=item["key"])
        r = requests.get(url)
        if r.status_code <= 300:
            _logger.debug("store %s success" % item["key"])
        else:
            _logger.error("store %s failed code: %s" % (item["key"],
                                                        r.status_code))

    @staticmethod
    def store_comment(item):
        comment = dict()
        comment["comment_id"] = item["comment_id"]
        comment["content"] = item["content"]
        comment["nickname"] = item["nickname"]
        comment["love"] = item["love"]
        comment["create_time"] = item["create_time"]
        comment["profile"] = item["profile"]
        comment["docid"] = item["docid"]
        url = COMMENT_STORE_API
        r = requests.post(url, json=comment)
        if r.status_code <= 300:
            _logger.debug("store %s success" % comment["comment_id"])
        else:
            _logger.warn("store %s failed code: %s" % (item["comment_id"],
                                                       r.status_code))














