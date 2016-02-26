# coding: utf-8

from scrapy.exceptions import DropItem
from News.items import NewsItem, CommentItem
from News.database import Base, session
News = Base.classes.news
Comment = Base.classes.newscomments


class PostgrePipeline(object):
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
