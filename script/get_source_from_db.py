# coding: utf-8

import os
import psycopg2 as DataBase

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-19 15:29"


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


def store(string):
    path = os.path.abspath(__file__)
    path = os.path.sep.join(path.split(os.path.sep)[:-2])
    with open(path+"/db_spider_sources.py", "w+") as f:
        f.write("SOURCE = "+string)


if __name__ == '__main__':
    sql = "select id, channel_name, channel_id, source_name, queue_name, frequency, source_url from spidersourcelist where status=1"
    rows = query(sql)
    store(rows.__repr__())

