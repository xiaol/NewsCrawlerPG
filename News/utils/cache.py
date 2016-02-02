from redis import Redis
from redis import from_url

from News.settings import REDIS_URL


class Cache(object):

    r = from_url(REDIS_URL) if REDIS_URL else Redis()

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





