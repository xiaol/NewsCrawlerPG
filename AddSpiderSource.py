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
SpiderQueueV2 = DBBase.classes.queuelist_v2
SpiderSource = DBBase.classes.spidersourcelist
SpiderSourceV2 = DBBase.classes.sourcelist_v2


PROJECT_NAME = "News"


def add_spider_queue(spider_name, queue_name):
    spider_queue = SpiderQueue(
        queue_name=queue_name,
        spider_name=spider_name,
        project_name=PROJECT_NAME,
    )

    spider_queue_v2 = SpiderQueueV2(
        queue=queue_name,
        spider=spider_name,
    )
    session = DBSession()
    try:
        session.add(spider_queue)
        session.add(spider_queue_v2)
        session.commit()
    except Exception as e:
        print(e.message)
        session.rollback()
    else:
        print("insert %s into spider queue list" % queue_name)


def get_spider_source_max_id():
    session = DBSession()
    spider_sources = session.query(SpiderSource.id, SpiderSource.source_url, SpiderSource.source_name).order_by(SpiderSource.id.desc())
    url_source_names = []
    max_id = spider_sources[0].id
    for source in spider_sources:
        url_source_names.append((source.source_url, source.source_name))
    return max_id, url_source_names


def add_spider_source(sources, spider_queue_name):
    for source in sources:
        max_id, url_source_names = get_spider_source_max_id()
        if (source["source_url"], source["source_name"]) in url_source_names:
            print("%s already in spider source list %s" % (source["source_name"], source["source_url"]))
            continue
        spider_source = SpiderSource(**source)
        spider_source.id = max_id + 1
        spider_source.queue_name = spider_queue_name
        spider_source.online = 0
        spider_source.create_time = datetime.now()
        spider_source.task_conf = {}
        # v2 code
        source_v2 = dict()
        source_v2['surl'] = source['source_url']
        source_v2['sname'] = source['source_name']
        source_v2['cname'] = source['channel_name']
        source_v2['cid'] = source['channel_id']
        source_v2['rate'] = source['frequency']
        source_v2['status'] = 0
        source_v2['state'] = 0
        spider_source_v2 = SpiderSourceV2(**source_v2)
        spider_source_v2.ctime = datetime.now()
        spider_source_v2.queue = spider_queue_name
        spider_source_v2.pconf = {}
        spider_source_v2.id = max_id + 1
        # end v2

        session = DBSession()
        try:
            session.add(spider_source)
            session.add(spider_source_v2)
            session.commit()
        except Exception as e:
            print(e.message)
            session.rollback()
        else:
            print("insert %s into spider source list %s" % (source["source_name"], source["descr"]))


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


