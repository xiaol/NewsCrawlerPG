# coding: utf-8

from urlparse import urljoin
from bs4 import BeautifulSoup
from scrapy import Spider, Request
from News.spiders import NewsSpider
from News.constans.www_adaymag_com import SPIDER_NAME, CRAWL_SOURCE
from News.items import NewsItem, get_default_news
from News.utils.util import g_cache_key, news_already_exists
from News.extractor import GeneralExtractor

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-28 17:28"


class Adamag(NewsSpider):

    name = SPIDER_NAME
    start_urls = ["http://www.adaymag.com/worldpost/fun/"]

    def g_news_meta_list(self, response):
        divs = response.xpath("//div[@class='td_mod_wrap td_mod8 ']")
        articles = list()
        for div in divs:
            article = {}
            thumb = div.xpath(".//div[@class='thumb-wrap']//img/@src").extract()
            item_details = div.xpath(".//div[@class='item-details']")
            if len(item_details) == 0:
                continue
            else:
                item_details = item_details[0]
            title = item_details.xpath(".//h3//text()").extract()
            url = item_details.xpath(".//h3/a/@href").extract()
            publish_time = item_details.xpath(".//div//time/@datetime").extract()
            summary = item_details.xpath(".//div[@class='td-post-text-excerpt']//text()").extract()
            if thumb and title and url and publish_time and summary:
                article["thumb"] = urljoin(base=response.url, url=thumb[0])
                article["title"] = title[0]
                article["url"] = url[0]
                p_time = publish_time[0]
                article["publish_time"] = p_time[:10] + " " + p_time[11:19]
                article["summary"] = summary[0]
                articles.append(article)
        return articles

    def g_news_item(self, article, start_url="", meta=None):
        crawl_url = article["url"]
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            title=article["title"],
            crawl_url=crawl_url,
            publish_time=article["publish_time"],
            summary=article["summary"],
            docid=crawl_url,
            key=key,
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
        )
        if meta is not None:
            news["meta_channel_id"] = meta["channel"]
            news["meta_channel_name"] = meta["name"]
            news["meta_channel_online"] = meta["online"]
        return news

    def parse_news(self, response):
        news = response.meta["news"]
        body = response.body_as_unicode().encode("utf-8")
        extractor = GeneralExtractor(body)
        title, post_date, post_user, summary, content = extractor()
        news["content"] = content
        yield news












