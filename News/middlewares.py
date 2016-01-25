import random
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from News.constans.useragent import WEB_USER_AGENT
from News.constans import yidianzixun


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", random.choice(WEB_USER_AGENT))
        if spider.name == yidianzixun.SPIDER_NAME:
            cookie = "JSESSIONID=constant-session-1;"
            request.headers.setdefault("Cookie", cookie)







