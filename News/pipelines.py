# coding: utf-8

import base64
from datetime import datetime, timedelta
import pymongo
import json
import requests
import logging
from scrapy.exceptions import DropItem

from News.items import NewsItem, CommentItem
from News.utils.cache import Cache
from News.utils.util import clean_date_time, replace_a_href_to_ours
from News.constans import NEWS_STORE_API, COMMENT_STORE_API
from News.monitor import monitor_news_in_pipeline
from News.monitor import monitor_news_store_success
from News.service import image
_logger = logging.getLogger(__name__)


class CompatiblePipeline(object):
    """为向后兼容， 对数据格式进行一些处理

    - 修改内容中 text 为 txt
    - 为 item 添加 image_number
    - 修改 txt 中的 a 标签为自己的链接

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
            for key, value in item.items():
                if key == "text":
                    value = replace_a_href_to_ours(value)
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
            cleaned_time = self.clean_post_date(item["publish_time"])
            if isinstance(cleaned_time, DropItem):
                raise cleaned_time
            else:
                item["publish_time"] = cleaned_time
            cleaned_content = self.clean_content(item["content"], item["image_number"], item["crawl_url"])
            if isinstance(cleaned_content, DropItem):
                raise cleaned_content
            else:
                item["content"] = cleaned_content
                return item
        elif isinstance(item, CommentItem):
            dt = clean_date_time(item['create_time'])
            if len(dt) == 0:
                raise DropItem("extractor datetime error %s" % item["publish_time"])
            return item
        else:
            return item

    @staticmethod
    def clean_post_date(string):
        now = datetime.now() + timedelta(days=1)
        dt = now.strftime("%Y-%m-%d %H:%M:%S")
        time = clean_date_time(string)
        if time > dt:
            return DropItem("extractor datetime error")
        else:
            return time

    def clean_content(self, content, image_number, url):
        cleaned = list()
        index = 1
        length = len(content)
        if url.startswith("http://mp.weixin.qq.com/"):
            for item in content:
                k, v = item.items()[0]
                if k == "txt":
                    if not self.is_dirty_text(v):
                        cleaned.append({k: v})
                elif k == "img":
                    if not self.is_dirty_image(v):
                        cleaned.append({k: v})
                else:
                    cleaned.append({k: v})
            return cleaned
        for i, item in enumerate(content, start=1):
            k, v = item.items()[0]
            if k == "txt":
                if not self.is_dirty_text(v):
                    cleaned.append({k: v})
            elif k == "img":
                if (index == 1 or index == image_number or 1.0*i/length >= 0.7) \
                        and self.is_dirty_image(v):
                    _logger.info("remove qr image: %s" % v)
                else:
                    cleaned.append({k: v})
                index += 1
            else:
                cleaned.append({k: v})
        if len(cleaned) == 0:
            return DropItem("content empty")
        return cleaned

    @staticmethod
    def is_dirty_text(string):
        return False

    @staticmethod
    def is_dirty_image(url):
        ad_set = {
            "http://mmbiz.qpic.cn/mmbiz/dyDu14T9ZVDQ5KyxY3BN9hDQVrne3BIeKz3l5AiaebgdkrO1YFFibYViaGbxzvZgKghLQo4yjkdEVF4licfOkMj8Aw/0?wx_fmt=png",
            "http://mmbiz.qpic.cn/mmbiz/dyDu14T9ZVDQ5KyxY3BN9hDQVrne3BIeKz3l5AiaebgdkrO1YFFibYViaGbxzvZgKghLQo4yjkdEVF4licfOkMj8Aw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1",
        }
        if url in ad_set:
            return True
        return image.is_dirty_image(url)


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
            "content_html": item.get("content_html", ""),
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
        Cache.expire(item["key"], 259200)   # 60*60*24*3
        return item


class MonitorPipeline(object):
    """ 添加监控信息　存入 redis

    redis key: spider:news:monitor:20160419
    存入爬虫源的id
    """
    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        info = item.get("start_meta_info")
        if info and info.get("source_id"):
            sid = info["source_id"]
            monitor_news_in_pipeline(sid)
        return item


class StartMetaPipeline(object):
    """ 处理传入的 meta 信息 """

    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        info = item.get("start_meta_info")
        if info:
            if isinstance(info.get("task_conf"), dict):
                info["task_conf"] = json.dumps(info["task_conf"])
            else:
                info["task_conf"] = json.dumps({})
            Cache.hmset(item["key"], info)
            return item
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
                info = item.get("start_meta_info")
                if info and info.get("source_id"):
                    sid = info["source_id"]
                    monitor_news_store_success(sid)
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
        comment["comment_id"] = str(item["comment_id"])
        comment["content"] = item["content"]
        comment["nickname"] = item["nickname"]
        comment["love"] = int(item["love"])
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
            meta = item.get("start_meta_info")
            if meta:
                print("source name: %s" % meta.get("source_name"))
                print("channel: %s" % meta.get("channel_name"))
            print("docid: %s" % item.get("docid"))
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
