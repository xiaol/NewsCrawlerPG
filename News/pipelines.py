# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import base64
import json
import logging
from datetime import datetime

import requests
from scrapy.exceptions import DropItem

from News.constans import CACHE_SOURCE_KEY
from News.constans import NEWS_STORE_API
from News.constans import COMMENT_STORE_API
from News.utils.cache import Cache
from News.items import NewsItem, CommentItem

_logger = logging.getLogger(__name__)


class CleanPipeline(object):
    pass


class CachePipeline(object):
    pass


class PostgrePipeline(object):
    pass


class MongoPipeline(object):
    pass


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
        obj["img_list"] = json.dumps(item["image_list"])
        obj["content"] = json.dumps(self._change_text_txt(item["content"]))
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
            Cache.expire(item["key"], 604800)  # 60*60*24*7
        else:
            raise DropItem("no spider info, start_url:%s" % start_url)

    @staticmethod
    def _change_text_txt(content):
        changed = list()
        for item in content:
            for key, value in item.iteritems():
                if key == "text":
                    changed.append({"txt": value})
                else:
                    changed.append({key: value})
        return changed

    @staticmethod
    def store_news(item):
        key = base64.encodestring(item["key"]).replace("=", "")
        url = NEWS_STORE_API.format(key=key)
        r = requests.get(url)
        if r.status_code <= 300:
            content = json.loads(r.content)
            if content["key"] == "succes":
                _logger.debug("store %s success" % item["key"])
            else:
                _logger.error("store failed: %s" % content["key"])
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


import pymongo


class MongoPipeline(object):

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://h44:27017,h213:27017,h241:27017/?replicaSet=myset")
        self.db = self.client["news_ver2"]
        self.collection = self.db["NewsItems"]

    def process_item(self, item, spider):
        if len(item["content"]) == 0:
            raise DropItem("content empty: %s" % item["crawl_url"])
        else:
            old = self.prepare_old_news_format(item)
            self.store_news(old)

    def store_news(self, old):
        inserted = self.collection.insert_one(old)
        print inserted.inserted_id

    def prepare_old_news_format(self, item):
        old = dict()
        item["content"] = self._change_text_txt(item["content"])
        item["content"] = self._change_content_compatible(item["content"])
        old["update_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old["sourceSiteName"] = item["crawl_source"]
        old["title"] = item["title"]
        old["url"] = item["crawl_url"]
        old["imgnum"] = item["image_number"]
        old["source_url"] = item["original_url"]
        old["content"] = item["content"]
        old["channel_id"] = "16"
        old["create_time"] = item["publish_time"]
        old["source"] = item["original_source"]
        old["channel"] = u"外媒观光团"
        return old

    @staticmethod
    def _change_content_compatible(content):
        old = list()
        for index, item in enumerate(content):
            old.append({str(index): item})
        return old

    @staticmethod
    def _change_text_txt(content):
        changed = list()
        for item in content:
            for key, value in item.iteritems():
                if key == "text":
                    changed.append({"txt": value})
                else:
                    changed.append({key: value})
        return changed













