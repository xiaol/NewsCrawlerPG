# coding: utf-8
from datetime import datetime

from bs4 import BeautifulSoup

from News.extractor import GeneralExtractor
from News.items import get_default_news
from News.spiders import NewsSpider
from News.constans.www_ettoday_net import SPIDER_NAME, ARTICLE_URL_TEMPLATE, CRAWL_SOURCE
from News.utils.util import g_cache_key


class Ettoday(NewsSpider):

    name = SPIDER_NAME

    title_param = {
        'method': 'find_all',
        'params': {'name': 'h2', 'attrs': {'class': 'title clearfix'}}
    }

    post_date_param = {
        'method': 'find_all',
        'params': {'name': 'span', 'attrs': {'class': 'news-time'}}
    }

    content_param = {
        'method': 'find_all',
        'params': {'name': 'div', 'attrs': {'class': 'story'}}
    }

    clean_content_after_param = {
        'method': 'find_all',
        'params': {'name': 'div', 'attrs': {'class': 'test-keyword'}}
    }

    def g_url_from_config(self, config):
        source_url = config['source_url'].split('/')[-1]
        url = ARTICLE_URL_TEMPLATE.format(**{'date': str(datetime.today()) + '-' + source_url})
        return url, ""

    def g_news_meta_list(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        tar_div = soup.find('div', id='all-news-list')
        items = tar_div.find_all('a')
        articles = list()
        for item in items:
            article = dict()
            article['title'] = item.text
            article['crawl_url'] = item['href']
            articles.append(article)
        return articles

    def g_news_item(self, article, start_url="", meta=None):
        crawl_url = article['crawl_url']
        key = g_cache_key(crawl_url)
        news = get_default_news(
            crawl_url=crawl_url,
            key=key,
            title=article['title'],
            love=article.get("like", 0),
            up=article.get("up", 0),
            original_url=article.get("url", ""),
            crawl_source=CRAWL_SOURCE,
            start_url=start_url,
            start_meta_info=meta,
            docid=crawl_url,
        )
        return news

    def parse_news(self, response):
        news = response.meta['news']
        redirects = response.request.meta.get("redirect_urls")
        if redirects:
            news["crawl_url"] = response.url
        body = response.body_as_unicode().encode("utf-8")
        extractor = GeneralExtractor(body, response.url)
        title, post_date, post_user, summary, content = extractor(
            title_param=self.title_param,
            post_date_param=self.post_date_param,
            content_param=self.content_param,
            clean_content_after_param=self.clean_content_after_param,
        )
        news['publish_time'] = post_date
        news['content'] = content
        news['content_html'] = response.body
        yield news
