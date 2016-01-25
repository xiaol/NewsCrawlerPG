# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
POSTGRES = "postgresql://postgres:lee@localhost/test"
Base = automap_base()
engine = create_engine(POSTGRES)
Base.prepare(engine, reflect=True)
News = Base.classes.newslist
session = Session(engine)


class NewsPipeline(object):
    def process_item(self, item, spider):
        print("title: %s" % item["title"])
        self.store_test(item)
        return item

    @staticmethod
    def g_api_object(item):
        pass

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


