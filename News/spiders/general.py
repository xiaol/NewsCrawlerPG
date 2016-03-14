# coding: utf-8

from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

from scrapy import cmdline

from News.items import get_default_news
from News.extractor import GeneralExtractor
from News.utils.util import g_cache_key
from News.spiders.config import configs


def parse_item(self, response):
    body = response.body_as_unicode().encode("utf-8")
    extractor = GeneralExtractor(body)
    title, post_date, post_user, summary, content = extractor(
        self.title_param, self.post_date_param, self.post_user_param,
        self.summary_param, self.content_param
    )
    if not post_user:
        post_user = self.crawl_source
    news = get_default_news(
        crawl_url=response.url,
        key=g_cache_key(response.url),
        title=title,
        publish_time=post_date,
        original_source=post_user,
        original_url=response.url,
        content=content,
        crawl_source=self.crawl_source,
    )
    print("*"*50)
    print("url: %s" % response.url)
    print("title: %s" % title)
    print("post date: %s" % post_date)
    print("post user: %s" % post_user)
    print("summary: %s" % summary)
    extractor.show(content)
    print("\n\n")


def news_spider_factory(start_urls, allowed_domains, rule, title_param,
                        post_date_param, post_user_param, summary_param,
                        content_param, db, channel_id, crawl_source,
                        *args, **kwargs):
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
        summary_param=summary_param,
        content_param=content_param,
        db=db,
        channel_id=channel_id,
        crawl_source=crawl_source,
    )
    return type(class_name, (CrawlSpider, ), class_attr)


mapping = locals()
for spider in configs:
    if spider["online"]:
        Test = news_spider_factory(**spider)
        mapping[Test.__name__] = Test
# cmdline.execute(argv=["python", "crawl", "spider:news:news_sina_com_cn"])










