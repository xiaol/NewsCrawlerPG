from redis import Redis


class Cache(object):

    r = Redis()

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





