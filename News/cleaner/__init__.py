# coding: utf-8
from lxml.html.clean import Cleaner

__author__ = "Sven Lee"
__copyright__ = "Copyright 2016-2019, ShangHai Lie Ying"
__credits__ = ["Sven Lee"]
__license__ = "Private"
__version__ = "1.0.0"
__email__ = "lee1300394324@gmail.com"
__date__ = "2016-04-05 22:20"


class BaseCleaner(Cleaner):
    scripts = True
    javascript = True
    comments = True
    style = True
    links = True
    meta = False
    page_structure = False
    processing_instructions = True
    embedded = False
    frames = False
    forms = False
    annoying_tags = False
    remove_unknown_tags = False
    safe_attrs_only = False
    add_nofollow = False


class NewsCleaner(BaseCleaner):
    allow_tags = (
        "html", "head", "title", "body",
        "div", "article",
        "p", "h1", "h2", "h3", "h4", "h5", "h6",
        "a", "img", "br", "font",
        "b", "blod", "big", "i", "em", "italic", "small", "strike", "sub",
        "strong", "sup", "strong", "tt", "u",
    )
    meta = True
    embedded = True
    frames = True
    forms = True



