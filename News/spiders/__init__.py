# coding: utf-8

# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

"""

    包含新闻爬虫基类 NewsSpider, 新闻配置爬虫基类 ConfigNewsSpider

"""

import abc
import six
from urlparse import urljoin
from scrapy import Request
from News.distributed import RedisMetaSpider
from News.items import get_default_news
from News.utils.util import g_cache_key, news_already_exists, load_json_data
from News.extractor import GeneralExtractor
from News.utils import load_object
from News.utils.util import get_date_time_default
from newsextractor import extract


@six.add_metaclass(abc.ABCMeta)
class NewsSpider(RedisMetaSpider):

    def parse(self, response):
        """
        解析 start url 返回的数据
        """

        meta = response.meta.get("start_meta", None)
        articles = self.g_news_meta_list(response)
        for article in articles:
            item = self.g_news_item(article, response.request.url, meta)
            if item is not None:
                yield self.g_news_request(item)

    @abc.abstractmethod
    def g_news_meta_list(self, response):
        """
        获取新闻 meta 信息列表, 抽象方法, 子类必须实现

        :return: meta info list
        """

    @abc.abstractmethod
    def g_news_item(self, article, start_url="", meta=None):
        """
        根据 meta 信息生成 News Item, 抽象方法, 子类必须实现

        :return: News Item or None
        """

    def g_news_request(self, item):
        """
        根据 News Item 生成内容页请求

        :return: Request Object
        """
        return Request(
            url=item["crawl_url"],
            callback=self.parse_news,
            meta={"news": item}
        )

    @abc.abstractmethod
    def parse_news(self, response):
        """
        解析内容页, 抽象方法, 子类必须实现
        """


class ConfigNewsSpider(NewsSpider):
    """

    新闻配置爬虫基类, 继承自 NewsSpider

    基类必须属性:
        name
        items_xpath
        title_xpath
        url_xpath
        crawl_source
    基类可选属性:
        ajax
        summary_xpath
        thumb_xpath
        title_param
        post_date_param
        post_source_param
        summary_param
        content_param
        extractor_cls

    """
    def g_news_meta_list(self, response):
        """
        根据配置文件中的 ajax 项, 使用不同策略解析 response 返回的数据
        :param response: scrapy 返回对象
        :type response: scrapy.Response
        :return: 解析得到的新闻信息
        :rtype: list[dict]

        """
        if hasattr(self, "ajax"):
            if self.ajax:
                return self.g_ajax_news_meta_list(response)
            else:
                return self.g_normal_news_meta_list(response)
        else:
            return self.g_normal_news_meta_list(response)

    def g_normal_news_meta_list(self, response):
        """
        正常情况, 返回内容为 HTML 格式, 使用 xpath 解析
        :param response: scrapy 返回对象
        :type response: scrapy.Response
        :return: 解析得到的新闻信息
        :rtype: list[dict]
        """
        base = response.url
        items = response.xpath(self.items_xpath)
        self.logger.info("items len: %s" % len(items))
        articles = list()
        for item in items:
            article = dict()
            title = item.xpath(self.title_xpath).extract()
            url = item.xpath(self.url_xpath).extract()
            if hasattr(self, "summary_xpath"):
                summary = item.xpath(self.summary_xpath).extract()
                if summary:
                    article["summary"] = summary[0]
            if hasattr(self, "thumb_xpath"):
                thumb = item.xpath(self.thumb_xpath).extract()
                if thumb:
                    article["thumb"] = urljoin(base, thumb[0])
            if title and url:
                article["title"] = title[0]
                article["url"] = urljoin(base, url[0])
                articles.append(article)
            else:
                self.logger.warning("title: %s, url: %s" % ("".join(title), "".join(url)))
        return articles

    def g_ajax_news_meta_list(self, response):
        """
        ajax 请求, 返回内容多为 json 格式, 根据配置信息, 定位相应数据段
        :param response: scrapy 返回对象
        :type response: scrapy.Response
        :return: 解析得到的新闻信息
        :rtype: list[dict]
        """
        body = load_json_data(response.body_as_unicode())
        if body is None:
            self.logger.warning("can't get data: url: %s body: %s" % (response.url, response.body_as_unicode()))
            return []
        items = self.get_dict_value(body, self.items_xpath)
        self.logger.info("item len: %s" % len(items))
        articles = list()
        for item in items:
            article = dict()
            article["title"] = self.get_dict_value(item, self.title_xpath)
            article["url"] = self.get_dict_value(item, self.url_xpath)
            if hasattr(self, "summary_xpath"):
                article["summary"] = self.get_dict_value(item, self.summary_xpath)
            if hasattr(self, "thumb_xpath"):
                article["thumb"] = self.get_dict_value(item, self.thumb_xpath)
            articles.append(article)
        return articles

    @staticmethod
    def get_dict_value(d, path):
        """
        根据 path 定位需要返回的数据, path 以 '|' 分隔
        :param d: 要定位数据的字典
        :type d: dict
        :param path: 以 '|' 分隔的路径
        :type path: str
        :return: 字典中的数据段
        :rtype: list
        """
        value = d
        for key in path.split("|"):
            value = value[key]
        return value

    def g_news_item(self, article, start_url="", meta=None):
        """
        生成 news item 对象
        :param article: 包含新闻 url, title 字段的字典
        :type article: dict
        :param start_url: 抓取 meta info 的起始 url
        :type start_url: str
        :param meta: 附加配置信息
        :type meta: dict
        :return: 新闻 Item
        :rtype: News.items.NewsItem | None
        """
        crawl_url = article["url"]
        key = g_cache_key(crawl_url)
        if news_already_exists(key):
            return None
        news = get_default_news(
            title=article["title"],
            crawl_url=crawl_url,
            docid=crawl_url,
            key=key,
            crawl_source=self.crawl_source,
            start_url=start_url,
            summary=article.get("summary", ""),
            start_meta_info=meta
        )
        return news

    def parse_news(self, response):
        """
        解析具体的新闻内容
        :param response: scrapy 返回对象
        :type response: scrapy.Response
        """
        news = response.meta["news"]
        body = response.body_as_unicode().encode("utf-8")
        title_param = self.title_param if hasattr(self, "title_param") else None
        post_date_param = self.post_date_param if hasattr(self, "post_date_param") else None
        post_source_param = self.post_source_param if hasattr(self, "post_source_param") else None
        summary_param = self.summary_param if hasattr(self, "summary_param") else None
        content_param = self.content_param if hasattr(self, "content_param") else None
        clean_param_list = self.clean_param_list if hasattr(self, "clean_param_list") else None
        clean_content_before_param = self.clean_content_before_param if hasattr(self, "clean_content_before_param") else None
        clean_content_after_param = self.clean_content_after_param if hasattr(self, "clean_content_after_param") else None
        news["content_html"] = body
        if content_param is None:   # 使用新闻解析包来解析
            try:
                title, post_date, post_user, summary, tags, content = extract(news["crawl_url"], document=body)
            except Exception as e:
                self.logger.warning(e.message + " newsextract error: %s" % news["crawl_url"])
            else:
                if content:
                    if not post_date:
                        post_date = get_date_time_default()
                    news["publish_time"] = post_date
                    news["content"] = content
                    if post_user:
                        news["original_source"] = post_user
                    yield news
                else:
                    self.logger.warning("publish_time or content empty: %s" % news["crawl_url"])
            return

        if hasattr(self, "extractor_cls"):
            extractor_cls = load_object(path=self.extractor_cls)
        else:
            extractor_cls = GeneralExtractor
        extractor = extractor_cls(body, response.url)
        title, post_date, post_user, summary, content = extractor(
            title_param=title_param,
            post_date_param=post_date_param,
            post_source_param=post_source_param,
            summary_param=summary_param,
            content_param=content_param,
            clean_param_list=clean_param_list,
            clean_content_before_param=clean_content_before_param,
            clean_content_after_param=clean_content_after_param,
        )
        news["publish_time"] = post_date
        news["content"] = content
        # test code
        title_spider_names = {
            'spider:news:www_people_com_cn',
            'spider:news:www_zaobao_com',
            'spider:news:www_chinatimes_com',
        }

        if self.name in title_spider_names:
            news['title'] = title
        # end test code
        yield news




