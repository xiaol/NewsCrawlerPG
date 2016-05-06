# coding: utf-8

from redis import from_url

from News.settings import REDIS_URL


class Cache(object):

    r = from_url(REDIS_URL, max_connections=3)

    @classmethod
    def exist(cls, key):
        return cls.r.exists(key)

    @classmethod
    def llen(cls, key):
        return cls.r.llen(key)

    @classmethod
    def lpush(cls, key, *args):
        return cls.r.lpush(key, *args)

    @classmethod
    def hmset(cls, key, maping):
        return cls.r.hmset(key, mapping=maping)

    @classmethod
    def hgetall(cls, key):
        return cls.r.hgetall(key)

    @classmethod
    def expire(cls, key, seconds):
        return cls.r.expire(key, seconds)

    @classmethod
    def sadd(cls, key, *args):
        return cls.r.sadd(key, *args)

    @classmethod
    def sismember(cls, key, value):
        return cls.r.sismember(key, value)





