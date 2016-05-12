#coding: utf-8
from bs4 import BeautifulSoup

from News.extractor import OushinetExtractor
from News.items import get_default_news
from News.spiders import NewsSpider
from News.utils.util import load_json_data, g_cache_key, news_already_exists
from News.constans.www_oushinet_com import SPIDER_NAME, CRAWL_SOURCE, ARTICLE_URL_TEMPLATE


class Oushinet(NewsSpider):

    name = SPIDER_NAME

    def g_news_meta_list(self, response):
        data = load_json_data(response.body[5:-3])
        if data is not None:
            ret = list()
            get_list = data.get("getList", [])
            soup = BeautifulSoup(get_list, 'lxml')
            lis = soup.find_all('li')
            for i in lis:
                item = dict()
                item['url'] = i.find('a')['href']
                item['title'] = i.find('a')['title']
                ret.append(item)
            return ret
        else:
            self.logger.warning("can't get data: url: %s body: %s" % (response.url, response.body_as_unicode()))
            return []

    def g_news_item(self, article, start_url="", meta=None):
        docid = article['url']
        crawl_url = self._g_article_url(article['url'])
        if not crawl_url:
            return None
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            crawl_url=crawl_url,
            key=key,
            title=article['title'],
            docid=docid,
            start_meta_info=meta,
            crawl_source=CRAWL_SOURCE
        )
        return news

    def parse_news(self, response):
        news = response.meta['news']
        body = response.body
        extractor = OushinetExtractor(body, response.url)
        title, post_date, post_user, summary, content = extractor()
        news['content'] = content
        # news['content_html'] = response.body
        news['publish_time'] = post_date
        yield news
        # exit()

    def _g_article_url(self, url):
        if not url:
            return None
        return ARTICLE_URL_TEMPLATE.format(url=url)