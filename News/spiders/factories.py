# coding: utf-8

from importlib import import_module
from News.spiders import ConfigNewsSpider
from News.constans import SPIDER_CONFIG_NAMES

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-03-30 15:06"


def config_news_factory(config):
    class_attr = dict(
        name=config.SPIDER_NAME,
        crawl_source=config.CRAWL_SOURCE,
        items_xpath=config.ITEMS_XPATH,
        title_xpath=config.TITLE_XPATH,
        url_xpath=config.URL_XPATH,
        __module__=__name__,
    )
    if hasattr(config, "START_URLS"):
        class_attr["start_urls"] = config.START_URLS
    if hasattr(config, "AJAX"):
        class_attr["ajax"] = config.AJAX
    if hasattr(config, "SUMMARY_XPATH"):
        class_attr["summary_xpath"] = config.SUMMARY_XPATH
    if hasattr(config, "THUMB_XPATH"):
        class_attr["thumb_xpath"] = config.THUMB_XPATH
    if hasattr(config, "TITLE_PARAM"):
        class_attr["title_param"] = config.TITLE_PARAM
    if hasattr(config, "POST_DATE_PARAM"):
        class_attr["post_date_param"] = config.POST_DATE_PARAM
    if hasattr(config, "POST_SOURCE_PARAM"):
        class_attr["post_source_param"] = config.POST_SOURCE_PARAM
    if hasattr(config, "SUMMARY_PARAM"):
        class_attr["summary_param"] = config.SUMMARY_PARAM
    if hasattr(config, "CONTENT_PARAM"):
        class_attr["content_param"] = config.CONTENT_PARAM
    if hasattr(config, "EXTRACTOR_CLS"):
        class_attr["extractor_cls"] = config.EXTRACTOR_CLS
    if hasattr(config, "CLASS_NAME"):
        class_name = config.CLASS_NAME
    else:
        class_name = "".join(map(str.capitalize, config.SPIDER_NAME.split(":")[-1].split("_"))) + "Spider"
    if hasattr(config, "CUSTOM_SETTINGS"):
        class_attr["custom_settings"] = config.CUSTOM_SETTINGS
    return type(class_name, (ConfigNewsSpider, ), class_attr)


mapping = locals()
for name in SPIDER_CONFIG_NAMES:
    cfg = import_module(name=name)
    cls = config_news_factory(config=cfg)
    mapping[cls.__name__] = cls




