# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from News.utils.cache import Cache


POSTGRES = "postgresql://postgres:lee@localhost/test"
Base = automap_base()
engine = create_engine(POSTGRES)
Base.prepare(engine, reflect=True)
News = Base.classes.newslist
session = Session(engine)


class NewsPipeline(object):
    def process_item(self, item, spider):
        print("title: %s" % item["title"])
        self.cache(item)
        self.store_test(item)
        return item

    @staticmethod
    def g_api_object(item):
        pass

    @staticmethod
    def cache(item):
        obj = dict()
        obj["key"] = item["key"]
        obj["url"] = item["crawl_url"]
        obj["docid"] = item["docid"]
        obj["title"] = item["title"]
        obj["keywords"] = json.dumps(item["tags"])
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
        Cache.hmset(item["key"], obj)

    @staticmethod
    def store_test(item):
        news = News(
            url=item["crawl_url"],
            docid=item["docid"],
            title=item["title"],
            tags=item["tags"],
            descr=item["summary"],
            love=item["love"],
            up=item["up"],
            author="",
            pub_url=item["original_url"],
            pub_name=item["original_source"],
            pub_time=item["publish_time"],
            img_num=item["image_number"],
            content=item["content"],
            content_html="",
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
            print("exists: %s" % item["title"])
        else:
            print("insert news: %s" % item["title"])


