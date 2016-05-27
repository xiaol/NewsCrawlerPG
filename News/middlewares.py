import random
import base64

from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from News.constans.useragent import WEB_USER_AGENT
from News.constans import yidianzixun


class RotateUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", random.choice(WEB_USER_AGENT))
        if spider.name == yidianzixun.SPIDER_NAME:
            cookie = "JSESSIONID=constant-session-1;"
            request.headers.setdefault("Cookie", cookie)


class WechatUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):
        browser = request.meta.get("browser")
        if not browser:
            # browser = random.choice(WEB_USER_AGENT)
            browser = WEB_USER_AGENT[0]
        request.headers.setdefault("User-Agent", browser)
        request.meta["browser"] = browser


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://47.88.1.21:3999'



