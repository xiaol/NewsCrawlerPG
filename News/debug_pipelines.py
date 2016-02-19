# coding: utf-8

import json
from scrapy.exceptions import DropItem

from News.items import NewsItem, CommentItem
from News.utils.cache import Cache
from News.database import Base, session
News = Base.classes.news
Comment = Base.classes.newscomments


class DebugPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, NewsItem):
            if len(item["content"]) == 0:
                raise DropItem("content empty:%s" % item["crawl_url"])
            else:
                self.cache_news(item)
                self.store_news(item)
        elif isinstance(item, CommentItem):
            self.store_comment(item)
        return item

    @staticmethod
    def cache_news(item):
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
        Cache.hmset(item["key"], obj)
        Cache.expire(item["key"], 604800)  # 60*60*24*7

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
            # print("exists: %s" % item["title"])
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


