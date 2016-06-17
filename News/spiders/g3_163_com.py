# coding: utf-8
import re
from scrapy import Request
from News.spiders import NewsSpider
from News.utils.util import load_json_data, news_already_exists, g_cache_key
from News.utils.util import str_from_timestamp
from News.items import NewsItem
from News.extractor.news163 import G3News163Extractor
from News.constans.g3_163_com import SPIDER_NAME
# from News.constans.news163 import COMMENT_SPIDER_NAME
from News.constans.g3_163_com import CRAWL_SOURCE
# from News.constans.news163 import ARTICLE_URL_TEMPLATE
# from News.constans.news163 import COMMENT_URL_TEMPLATE
from News.constans.g3_163_com import DOMAIN
# from News.extractor import News163Extractor


class G3News163(NewsSpider):

    name = SPIDER_NAME
    default_comment_count = 30

    def g_news_meta_list(self, response):
        ret_content = response.body
        data = load_json_data(ret_content)
        keys = data.keys()
        articles = data[keys[0]]
        if articles is None:
            self.logger.error("spider has been banned for %s" % response.request.url)
            return []
        else:
            return articles

    def g_news_item(self, article, start_url="", meta=None):
        news = NewsItem()
        news["docid"] = article["docid"]
        news["crawl_url"] = self._g_crawl_url(news['docid'])
        news["key"] = g_cache_key(news["crawl_url"])
        if news_already_exists(news["key"]): return None
        news["title"] = article["title"]
        if 'ltitle' in news and news['ltitle']:
            news['summary'] = article['ltitle']
        news["tags"] = list()
        news["publish_time"] = article["ptime"]
        news["content"] = list()
        news["love"] = 0
        news["up"] = 0
        news["down"] = 0

        news["crawl_source"] = CRAWL_SOURCE
        news['original_url'] = ''
        news["original_source"] = article.get('source', '')
        # news["comment_url"] = self._g_comment_url(docid=news["docid"])
        news["start_url"] = start_url
        news["start_meta_info"] = meta
        return news

    def g_news_request(self, item):
        url =item['crawl_url']
        # item["docid"] = item["doci"]
        return Request(
                url=url,
                callback=self.parse_news,
                meta={"news": item}
        )

    def parse_news(self, response):
        news = response.meta["news"]
        data = load_json_data(response.body_as_unicode().encode('utf8'))
        data = data[news['docid']]
        if data and data.get("body"):
            data['body'] = '<div id="inner_article">' + data["body"] + "</div>"
            keyword = u'您的新闻客户端版本太低啦，升级之后就能看到更丰富的新闻形式了'
            if keyword in data['body']:
                return
            # title, post_date, post_user, summary, content = extractor()
            # news["content"] = content
            # news["content_html"] = body
            # if len(news["content"]) == 0:
            #     return
            # else:
            #     yield newsii
            content_html = data['body']
            if 'img' in data and data['img']:
                content_html = self._replace_img_tag_in_html(data)
                print data
            news['content_html'] = content_html

            extractor = G3News163Extractor(content_html)
            title, post_date, post_user, summary, content = extractor()
            news['content'] = content
            if len(news['content']) == 0:
                return
            else:
                yield news

        else:
            self.logger.warning("can't get content url: %s body: %s" % (response.url, response.body_as_unicode()))

    @staticmethod
    def _g_crawl_url(docid):
        return 'http://c.3g.163.com/nc/article/%s/full.html' % docid



    @staticmethod
    def _replace_img_tag_in_html(data):
        pattern = re.compile(r'(<!--IMG#[0-9]+-->)')
        img_tags = pattern.findall(data['body'])
        ret = data['body']
        for i in img_tags:
            for j in data['img']:
                if j['ref'] == i:
                    ret = ret.replace(i, '<img src="%s">'%j['src'])
                    break
        return ret






