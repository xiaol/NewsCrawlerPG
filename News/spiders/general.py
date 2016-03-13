# coding: utf-8

from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from scrapy import cmdline

from News.extractor import GeneralExtractor


def parse_item(self, response):
    body = response.body_as_unicode().encode("utf-8")
    extractor = GeneralExtractor(body)
    title, post_date, post_user, content = extractor(self.title_param,
                                                     self.post_date_param,
                                                     self.post_user_param,
                                                     self.content_param)
    print("*"*50)
    print("url: %s" % response.url)
    print("title: %s" % title)
    print("post date: %s" % post_date)
    print("post user: %s" % post_user)
    extractor.show(content)
    print("\n\n")


spider = {
    "allowed_domains": ["news.sina.com.cn"],
    "start_urls": ["http://news.sina.com.cn/society/"],
    "rule": {
        "follow_allow": [r"^http://news\.sina\.com\.cn/[a-z0-9A-Z]\w*/$"],
        "follow_deny": [],
        "parse_allow": [r"^http://\S*news\.sina\.com\.cn/\S*\d{4}-\d{2}-\d{2}/\S*\.shtml$"],
        "parse_deny": ["http://\S*news.sina.com.cn/\S*video\d{4}-\d{2}-\d{2}/\S*\.shtml$"],
    },
    "title_param": {"name": None, "attrs": {"id": "artibodyTitle"}},
    "post_date_param": {"name": None, "attrs": {"class": "time-source"}},
    "post_user_param": {"name": "meta", "attrs": {"name": "mediaid"}},
    "content_param": {"name": None, "attrs": {}},
}


def news_spider_factory(start_urls, allowed_domains, rule, title_param,
                        post_date_param, post_user_param, content_param):
    words = allowed_domains[0].split(".")
    class_name = "".join(map(str.capitalize, words)) + "Spider"
    spider_name = "spider:news:" + "_".join(words)
    rules = []
    if rule["follow_allow"] or rule["follow_deny"]:
        rules.append(Rule(LinkExtractor(allow=tuple(rule["follow_allow"]), deny=tuple(rule["follow_deny"])), follow=True))
    if rule["parse_allow"] or rule["parse_allow"]:
        rules.append(Rule(LinkExtractor(allow=tuple(rule["parse_allow"]), deny=tuple(rule["parse_deny"])), callback="parse_item"))
    class_attr = dict(
        name=spider_name,
        allowed_domains=allowed_domains,
        start_urls=start_urls,
        rules=tuple(rules),
        parse_item=parse_item,
        title_param=title_param,
        post_date_param=post_date_param,
        post_user_param=post_user_param,
        content_param=content_param,
    )
    return type(class_name, (CrawlSpider, ), class_attr)


def general_spider_factory(name, class_name, allowed_domains, start_urls, rules):
    attr = dict(name=name, allowed_domains=allowed_domains,
                start_urls=start_urls, rules=rules, parse_item=parse_item)
    X = type(class_name, (CrawlSpider, ), attr)
    return X


mapping = locals()

# allowed_domains = ["news.sina.com.cn"]
# start_urls = ["http://news.sina.com.cn/society/"]
# allow = ("http://\.*news\.sina\.com\.cn/[a-z]/\d{4}-\d{2}-\d{2}/.*\.shtml", )
# allow = ("http://news\.sina\.com\.cn/s/2015-07-08/223232087218\.shtml", )
# rules = (Rule(LinkExtractor(allow=allow), callback="parse_item"),)
# words = allowed_domains[0].split(".")
# class_name = "".join(map(str.capitalize, words)) + "Spider"
# name = "spider:news:" + "_".join(words)
#
# Test = general_spider_factory(name, class_name, allowed_domains, start_urls, rules)
# mapping[Test.__name__] = Test
#
# cmdline.execute(argv=["python", "crawl", name])

Test = news_spider_factory(**spider)
mapping[Test.__name__] = Test
cmdline.execute(argv=["python", "crawl", "spider:news:news_sina_com_cn"])










