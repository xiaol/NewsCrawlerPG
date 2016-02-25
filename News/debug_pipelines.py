# coding: utf-8

from datetime import datetime
import pymongo
import json
from scrapy.exceptions import DropItem

from News.items import NewsItem, CommentItem
from News.utils.cache import Cache
from News.database import Base, session
News = Base.classes.news
Comment = Base.classes.newscomments


class CompatiblePipeline(object):
    """为先后兼容， 对数据格式进行一些处理"""

    def process_item(self, item, spider):
        if not isinstance(item, NewsItem):
            return item
        item["content"] = self._change_text_txt(item["content"])
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


class CleanPipeline(object):
    """清洗数据， 丢弃不完整的数据"""

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            if len(item["content"]) == 0:
                raise DropItem("content empty: %s" % item["crawl_url"])
            else:
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
            "docid": item["docid"],
            "title": item["title"],
            "keywords": ",".join(item["tags"]),
            "synopsis": item["summary"],
            "love": item["love"],
            "up": item["up"],
            "author": "",
            "pub_url": item["original_url"],
            "pub_name": item["original_source"],
            "pub_time": item["publish_time"],
            "img_num": item["image_number"],
            "img_list": json.dumps(item["image_list"]),
            "content": json.dumps(item["content"]),
            "content_html": "",
        }
        if item.get("province"):
            obj["province"] = item["province"]
        if item.get("city"):
            obj["city"] = item["city"]
        if item.get("district"):
            obj["district"] = item["district"]
        Cache.hmset(item["key"], obj)
        Cache.expire(item["key"], 604800)
        return item


class PostgrePipeline(object):
    """数据入 postgres 数据库"""

    pass


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
        formated = self.__prepare_mongo_format(item)
        self.collection.update({"title": formated["title"]},
                               {"$setOnInsert": formated},
                               upsert=True)

    @classmethod
    def __prepare_mongo_format(cls, item):
        old = dict()
        item["content"] = cls.__change_content_compatible(item["content"])
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
    def __change_content_compatible(content):
        old = list()
        for index, item in enumerate(content):
            old.append({str(index): item})
        return old


class DebugPostgrePipeline(object):
    """本地测试入 postgres 数据"""

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
        news = News(
            key=item["key"],
            title=item["title"],
            tags=item["tags"],
            summary=item["summary"],
            publish_time=item["publish_time"],
            content=item["content"],
            love=item["love"],
            up=item["up"],
            down=item["down"],
            image_number=item["image_number"],

            docid=item["docid"],
            channel=item["channel"],
            category=item["category"],
            crawl_url=item["crawl_url"],
            original_url=item["original_url"],
            crawl_source=item["crawl_source"],
            original_source=item["original_source"],
        )
        if item.get("province"):
            news.province = item["province"]
        if item.get("city"):
            news.city = item["city"]
        if item.get("district"):
            news.district = item["district"]
        try:
            session.add(news)
            session.commit()
        except:
            session.rollback()
        else:
            print("insert news: %s" % item["title"])

    @staticmethod
    def store_comment(item):
        comment = Comment(
            comment_id=item["comment_id"],
            content=item["content"],
            nickname=item["nickname"],
            love=item["love"],
            create_time=item["create_time"],
            profile=item["profile"],
            docid=item["docid"],
        )
        try:
            session.add(comment)
            session.commit()
        except Exception as e:
            print("error: %s" % e.message)
            session.rollback()