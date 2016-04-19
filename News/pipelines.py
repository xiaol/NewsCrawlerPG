# coding: utf-8

import base64
from datetime import datetime
import pymongo
import json
import requests
import logging
from scrapy.exceptions import DropItem

from News.items import NewsItem, CommentItem
from News.utils.cache import Cache
from News.utils.util import clean_date_time
from News.constans import NEWS_STORE_API, CACHE_SOURCE_KEY, COMMENT_STORE_API

_logger = logging.getLogger(__name__)


class CompatiblePipeline(object):
    """为向后兼容， 对数据格式进行一些处理

    - 修改内容中 text 为 txt
    - 为 item 添加 image_number

    """

    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        item["content"] = self._change_text_txt(item["content"])
        item["image_number"] = self._get_image_number(item["content"])
        return item

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
    def _get_image_number(content):
        n = 0
        for c in content:
            if "img" in c:
                n += 1
        return n


class CleanPipeline(object):
    """清洗内容为空或时间格式不正确的新闻, 统一时间格式
    """

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            if len(item["content"]) == 0:
                raise DropItem("content empty: %s" % item["crawl_url"])
            else:
                dt = clean_date_time(item["publish_time"])
                if len(dt) == 0:
                    raise DropItem("extractor datetime error %s" % item["publish_time"])
                else:
                    item["publish_time"] = dt
                    return item
        elif isinstance(item, CommentItem):
            dt = clean_date_time(item['create_time'])
            if len(dt) == 0:
                raise DropItem("extractor datetime error %s" % item["publish_time"])
            return item
        else:
            return item


class CachePipeline(object):
    """缓存新闻数据"""

    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        obj = {
            "key": item["key"],
            "url": item["crawl_url"],
            "title": item["title"],
            "keywords": ",".join(item["tags"]),
            "author": "",
            "pub_time": item["publish_time"],
            "pub_name": item["original_source"] or item["crawl_source"],
            "pub_url": item["original_url"] or item["crawl_url"],
            "content_html": "",
            "synopsis": item["summary"],
            "img_num": item["image_number"],
            "up": item["up"],
            "love": item["love"],
            "docid": item["docid"],
            "content": json.dumps(item["content"]),
        }
        if item.get("comment_queue") and item.get("comment_url"):
            obj["comment_queue"] = item["comment_queue"]
            obj["comment_task"] = item["comment_url"]
        if item.get("province"):
            obj["province"] = item["province"]
        if item.get("city"):
            obj["city"] = item["city"]
        if item.get("district"):
            obj["district"] = item["district"]
        Cache.hmset(item["key"], obj)
        Cache.expire(item["key"], 604800)   # 60*60*24*7
        return item


class StartMetaPipeline(object):
    """ 处理传入的 meta 信息 """

    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        info = item.get("start_meta_info")
        if info:
            Cache.hmset(item["key"], info)
        else:
            raise DropItem("no start meta info")


class StorePipeline(object):
    """调用远端存储服务， 数据入数据库"""

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            self.store_news(item)
        elif isinstance(item, CommentItem):
            self.store_comment(item)
        else:
            raise DropItem("unknown item type: %s" % type(item))
        return item

    @staticmethod
    def store_news(item):
        """调用远端的存储服务，存储缓存中的新闻。

        注意： 传递给服务端的参数是缓存中的 key, 需要通过 base64 编码后传递
        """
        key = base64.encodestring(item["key"]).replace("=", "")
        url = NEWS_STORE_API.format(key=key)
        r = requests.get(url)
        if r.status_code <= 300:
            content = json.loads(r.content)
            if content["key"] == "succes":
                _logger.info("store %s success" % item["key"])
            else:
                _logger.error("store failed: %s" % content["key"])
        else:
            _logger.error("store %s failed code: %s" % (item["key"],
                                                        r.status_code))

    @staticmethod
    def store_comment(item):
        """调用远端的存储服务，存储 post 过去的评论数据"""
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


class MongoPipeline(object):
    """数据入 mongodb 数据库"""

    def __init__(self, mongo_uri, mongo_db, mongo_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_collection = mongo_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db=crawler.settings.get("MONGO_DATABASE"),
            mongo_collection=crawler.settings.get("MONGO_COLLECTION")
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.collection = self.db[self.mongo_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        formated = self.__prepare_mongo_format(item, spider)
        self.collection.update({"title": formated["title"]},
                               {"$setOnInsert": formated},
                               upsert=True)
        _logger.info("store %s in mongodb" % formated["title"])
        return item

    @classmethod
    def __prepare_mongo_format(cls, item, spider):
        old = dict()
        item["content"] = cls.__change_content_compatible(item["content"])
        old["update_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old["sourceSiteName"] = item["original_source"]
        old["title"] = item["title"]
        old["url"] = item["crawl_url"]
        old["imgnum"] = item["image_number"]
        old["source_url"] = item["original_url"]
        old["content"] = item["content"]
        old["create_time"] = item["publish_time"]
        old["source"] = item["original_source"]

        # old["channel_id"] = item["meta_channel_id"]
        # old["channel"] = item["meta_channel_name"]
        return old

    @staticmethod
    def __change_content_compatible(content):
        old = list()
        for index, item in enumerate(content):
            old.append({str(index): item})
        return old


class PrintPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            print("*" * 50)
            print("title: %s" % item["title"])
            print("url: %s" % item["crawl_url"])
            print("date: %s" % item["publish_time"])
            print("user: %s" % item["original_source"])
            print("channel: %s" % item.get("meta_channel_name", ""))
            for i in item["content"]:
                for key, value in i.items():
                    print("%s: %s" % (key, value))
            print("\n")
            if item.get("comment_queue") and item.get("comment_url"):
                self.test_comment_spider(item)

        elif isinstance(item, CommentItem):
            print("*" * 50)
            # print("id: %s" % item["comment_id"])
            print("content: %s" % item["content"])
            print("create_time: %s" % item["create_time"])
            # print("nickname: %s" % item["nickname"])
            # print("profile: %s" % item['profile'])
            # print("love: %s" % item['love'])
            print("docid: %s" % item['docid'])
            # print("\n")

    def test_comment_spider(self, item):
        queue = item.get("comment_queue")
        url = item.get("comment_url")
        if queue and url:
            Cache.lpush(queue, url)
            _logger.info("push {url} in {queue}".format(url=url, queue=queue))
