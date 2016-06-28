# coding: utf-8

import json
from urlparse import urljoin
import re
from datetime import datetime, timedelta
from News.spiders import NewsSpider
from News.utils.util import g_cache_key, news_already_exists
from News.utils.util import str_from_timestamp
from News.items import get_default_news
from News.constans.wechat import SPIDER_NAME
from News.constans.wechat import COMMENT_SPIDER_NAME
from News.constans.wechat import CRAWL_SOURCE
from News.extractor import WechatExtractor
from News.scheduler import wechat
from newsextractor import extract


class Wechat(NewsSpider):

    name = SPIDER_NAME
    custom_settings = {
        "DOWNLOAD_DELAY": 10,
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy.downloadermiddlewares.cookies.CookiesMiddleware": 700,
            "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
            "News.middlewares.RotateUserAgentMiddleware": None,
            "News.middlewares.WechatUserAgentMiddleware": 405,
            # 'News.middlewares.ProxyBanMiddleware': 100,
        },
    }

    def g_url_from_config(self, config):
        meta = config["meta"]
        source_name = meta["source_name"].split(";")
        name = source_name[0]
        oid = source_name[1]
        return wechat.get_start_url(name, oid)

    def clean_script_data(self, string):
        mapping = [
            ("\\\\", ""),
            ("&quot;", '"'),
            ("&amp;", "&"),
        ]
        for k, v in mapping:
            string = string.replace(k, v)
        return string

    def clean_escape_data(self, string):
        mapping = {
            "&quot;": '"',
            "&amp;": "&",
            "&lt;": "<",
            "&gt;": ">",
            "&nbsp;": " ",
            "&cent;": u"¢",
            "&pound;": u"£",
            "&yen;": u"¥",
            "&euro;": u"€",
            "&copy;": u"©",
            "&reg;": u"®",
        }
        for k, v in mapping.items():
            string = string.replace(k, v)
        return string

    def g_news_meta_list(self, response):
        p = "var msgList = '([^']*)';"
        match = re.search(p, response.body)
        if match is None:
            return []
        data = match.group(1)
        if not data:
            return []
        data = self.clean_script_data(data)
        data_list = json.loads(data)
        data_list = data_list["list"]
        articles = []
        for item in data_list:
            comm_msg_info = item["comm_msg_info"]
            publish_time = str_from_timestamp(comm_msg_info["datetime"])
            today = datetime.now() - timedelta(days=2)
            today_string = today.strftime("%Y-%m-%d %H:%M:%S")
            if publish_time < today_string:
                self.logger.info("%s < %s" % (publish_time, today_string))
                continue
            app_msg_ext_info = item["app_msg_ext_info"]
            article = {
                "title": app_msg_ext_info["title"],
                "summary": app_msg_ext_info.get("digest", ""),
                "crawl_url": app_msg_ext_info["content_url"],
                "publish_time": publish_time,
                "thumb": app_msg_ext_info.get("cover", ""),
            }
            articles.append(article)
            for msg in app_msg_ext_info.get("multi_app_msg_item_list", []):
                article = {
                    "title": msg["title"],
                    "summary": msg.get("digest", ""),
                    "crawl_url": msg["content_url"],
                    "publish_time": publish_time,
                    "thumb": msg.get("cover", "")
                }
                articles.append(article)
        for article in articles:
            article["title"] = self.clean_escape_data(article["title"])
            article["summary"] = self.clean_escape_data(article["summary"])
            article["crawl_url"] = self.clean_escape_data(urljoin(response.url, article["crawl_url"]))
            article["thumb"] = self.clean_escape_data(article["thumb"])
        return articles

    def g_news_item(self, article, start_url="", meta=None):
        crawl_url = article["crawl_url"]
        comment_url = self._g_comment_url(crawl_url)
        news = get_default_news(
            crawl_url=crawl_url,
            docid=comment_url,
            key=g_cache_key(article["title"].encode("utf-8")),
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
            summary=article["summary"],
            publish_time=article["publish_time"],
            title=article["title"],
            start_meta_info=meta,
            comment_url=comment_url,
            comment_queue=COMMENT_SPIDER_NAME+":start_urls"
        )
        return None if news_already_exists(news["key"]) else news

    def parse_news(self, response):
        news = response.meta["news"]
        redirects = response.request.meta.get("redirect_urls")
        if redirects:
            news["crawl_url"] = response.url
        body = response.body_as_unicode().encode("utf-8")
        title, post_date, post_user, summary, tags, content = extract(news["crawl_url"], document=body)
        # extractor = WechatExtractor(body, response.url)
        # title, post_date, post_user, summary, content = extractor()
        news["title"] = title
        news["publish_time"] = post_date
        news["original_source"] = post_user
        news["original_url"] = news["crawl_url"]
        news["content"] = content
        news["content_html"] = response.body
        yield news

    @staticmethod
    def _g_comment_url(url):
        prefix = "http://mp.weixin.qq.com/mp/getcomment"
        try:
            index = url.index("?")
        except ValueError:
            return ""
        else:
            return prefix+url[index:]

