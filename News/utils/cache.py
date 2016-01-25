from redis import Redis


class Cache(object):

    r = Redis()

    @classmethod
    def exist(cls, key):
        return cls.r.exists(key)





