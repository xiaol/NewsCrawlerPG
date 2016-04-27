# coding: utf-8

"""
通过配置文件路径，添加抓取源到 postgres
"""

from importlib import import_module
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.automap import automap_base

from News.scheduler import g_queue_name
from News.scheduler.sources import g_spider_source

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-13 10:34"


POSTGRES = "postgresql://postgres:ly@postgres&2015@120.27.163.25/BDP"
DBBase = automap_base()
engine = create_engine(POSTGRES, convert_unicode=True)
DBBase.prepare(engine, reflect=True)
DBSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

SpiderQueue = DBBase.classes.spiderqueuelist
SpiderSource = DBBase.classes.spidersourcelist


PROJECT_NAME = "News"


def add_spider_queue(spider_name, queue_name):
    spider_queue = SpiderQueue(
        queue_name=queue_name,
        spider_name=spider_name,
        project_name=PROJECT_NAME,
    )
    session = DBSession()
    try:
        session.add(spider_queue)
        session.commit()
    except Exception as e:
        print(e.message)
        session.rollback()
    else:
        print("insert %s into spider queue list" % queue_name)


def get_spider_source_max_id():
    session = DBSession()
    spider_sources = session.query(SpiderSource).order_by(SpiderSource.id.desc())
    urls = []
    max_id = spider_sources[0].id
    for source in spider_sources:
        urls.append(source.source_url)
    return max_id, urls


def add_spider_source(sources, spider_queue_name):
    for source in sources:
        max_id, urls = get_spider_source_max_id()
        if source["source_url"] in urls:
            print("%s already in spider source list" % source["source_url"])
            continue
        spider_source = SpiderSource(**source)
        spider_source.id = max_id + 1
        spider_source.queue_name = spider_queue_name
        spider_source.online = 0
        spider_source.create_time = datetime.now()
        spider_source.task_conf = {}
        session = DBSession()
        try:
            session.add(spider_source)
            session.commit()
        except Exception as e:
            print(e.message)
            session.rollback()
        else:
            print("insert %s into spider source list" % source["descr"])


if __name__ == '__main__':
    while 1:
        path = raw_input("please input spider config path: ").strip()
        try:
            cfg = import_module(path)
        except ImportError:
            break
        spider_name = cfg.SPIDER_NAME
        categories = cfg.CATEGORIES
        source_name = cfg.CRAWL_SOURCE
        spider_queue_name = g_queue_name(spider_name)

        sources = g_spider_source(categories, source_name)
        while 1:
            print("""
            1. add spider queue
            2. add spider source
            """)
            command = int(raw_input("please input command index: ").strip())
            if command == 1:
                add_spider_queue(spider_name, spider_queue_name)
            elif command == 2:
                add_spider_source(sources, spider_queue_name)
            else:
                break


