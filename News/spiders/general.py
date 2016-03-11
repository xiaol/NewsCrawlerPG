# coding: utf-8

from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from News.extractor import GeneralExtractor


def parse_item(self, response):
    body = response.body_as_unicode().encode("utf-8")
    extractor = GeneralExtractor(body)
    title, post_date, post_user, content = extractor()
    print("*"*50)
    print("url: %s" % response.url)
    print("title: %s" % title)
    print("post date: %s" % post_date)
    print("post user: %s" % post_user)
    extractor.show(content)
    print("\n\n")


def general_spider_factory(allowed_domains, start_urls, rules):
    words = allowed_domains[0].split(".")
    class_name = "".join(map(str.capitalize, words)) + "Spider"
    name = "spider:news:" + "_".join(words)
    attr = dict(name=name, allowed_domains=allowed_domains,
                start_urls=start_urls, rules=rules, parse_item=parse_item)
    X = type(class_name, (CrawlSpider, ), attr)
    return X


mapping = locals()

allowed_domains = ["news.sina.com.cn"]
start_urls = ["http://news.sina.com.cn/society/"]
allow = "http://\.*news\.sina\.com\.cn/[a-z]/\d{4}-\d{2}-\d{2}/.*\.shtml"
allow = "http://news\.sina\.com\.cn/s/2015-07-08/223232087218\.shtml"
rules = (Rule(LinkExtractor(allow=(allow, )), callback="parse_item"),)

Test = general_spider_factory(allowed_domains, start_urls, rules)
mapping[Test.__name__] = Test












