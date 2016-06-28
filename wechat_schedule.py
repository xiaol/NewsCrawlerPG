# coding: utf-8
import os
import psycopg2 as DataBase
import json
import time
import random

#test
# from redis import Redis

from News.utils.cache import Cache

DBName = "BDP"
User = "postgres"
Host = "120.27.163.25"
Password = "ly@postgres&2015"
connection = DataBase.connect(database=DBName,
                              user=User,
                              password=Password,
                              host=Host)


def query(sql):
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


def get_wechat_source():
    sql = '''
    SELECT id, channel_name, channel_id, source_name, queue_name, frequency, source_url, online
    FROM spidersourcelist where status=1 and queue_name='spider:news:wechat:start_urls'
    '''
    rows = query(sql)
    return rows

def get_schedule_queue():
    """ 从数据库调度源获取调度信息，生成调度队列 """
    SOURCE = get_wechat_source()
    schedule_queue = list()
    for source in SOURCE:
        request = dict()
        request["sid"] = source[0]
        request["surl"] = source[6]
        meta = dict()
        meta["cid"] = source[2]
        # meta["channel_name"] = source[1]
        meta["sname"] = source[3]
        meta["pconf"] = {}
        meta["state"] = source[7]
        request["meta"] = meta
        r = json.dumps(request)
        queue_name = source[4]
        frequency = source[5]
        schedule_queue.append(
            {
                "time": int(time.time()),
                "queue": queue_name,
                "interval": frequency*60,
                "request": r,
                "running": False,
            }
        )
    return schedule_queue


def push_request_to_queue(queue, request):
    print(request)
    Cache.lpush(queue, request)
    # r = Redis()
    # r.lpush(queue, request)


def run():
    scheduler_info_list = get_schedule_queue()
    info_length = len(scheduler_info_list)
    average = 60*60*24/info_length - 15
    for index, info in enumerate(scheduler_info_list):
        push_request_to_queue(info['queue'], info['request'])
        time.sleep(average)

if __name__ == '__main__':
    run()
