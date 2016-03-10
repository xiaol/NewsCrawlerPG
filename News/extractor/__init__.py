# coding: utf-8
import re
from lxml import html
from lxml.html.clean import Cleaner
from bs4 import BeautifulSoup, Comment, Tag, NavigableString


class NewsExtractor(object):

    HARD_TAGS = ["strong", "em", "a"]
    TAGS = ["script", "link"]

    def __init__(self, html, url=None, hard_tags=None, tags=None, news=None):
        self.html = html
        self.cleaned_html = html
        self.url = url
        self.hard_tags = hard_tags if hard_tags is not None else self.HARD_TAGS
        self.tags = tags if tags is not None else self.TAGS
        self._hard_remove_tags()
        self.soup = BeautifulSoup(self.cleaned_html, "lxml")
        self._remove_comments()
        self._remove_tags()
        self.news = news

    def _hard_remove_tags(self):
        """ remove tags in html, notice not remove the inner content """
        if self.hard_tags:
            p = re.compile("|".join(["<{tag}[^>]*>|</{tag}>".format(tag=tag)
                                     for tag in self.hard_tags]))
            self.cleaned_html = re.sub(p, "", self.html)

    def _remove_comments(self):
        """ remove comments in html """
        comments = self.soup.find_all(text=lambda text: isinstance(text, Comment))
        [comment.extract() for comment in comments]

    def _remove_tags(self):
        """ remove tags and inner content in html """
        [tag.extract() for tag in self.soup.find_all(self.tags)]

    @staticmethod
    def _remove_tag(tag, name, **kwargs):
        """
        remove all tags in Tag of BeautifulSoup
        :param tag: Tag Object of BeautifulSoup
        :param name: str, tag name
        :param kwargs: parameters of find_all
        :return: in place, no return
        """
        if tag is None: return
        [t.extract() for t in tag.find_all(name, **kwargs)]

    @staticmethod
    def g_returns(content):
        count = 0
        contents = list()
        for c in content:
            if "img" in c and c["img"]:
                count += 1
                contents.append(c)
            elif "text" in c and c["text"] and c["text"].strip():
                contents.append(c)
        return contents, count

    @classmethod
    def _extract(cls, tag):
        result = list()
        if not tag: return result
        for child in tag.descendants:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                if child.name == "img":
                    result.append({"img": cls.__get_img_src(child)})
            else:
                pass
        return result

    @classmethod
    def _extract_regular(cls, tag, length=3):
        result = list()
        tag, l = cls._get_content_tag(tag)
        if tag is None or l < length:
            return result
        cls._extract_tag_children(tag, result)
        return result

    @classmethod
    def _extract_tag_children(cls, tag, result):
        for child in tag.children:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                if child.name == "img":
                    result.append({"img": cls.__get_img_src(child)})
                elif child.img:
                    cls._extract_tag_children(child, result)
                else:
                    result.append({"text": child.get_text().strip()})
            else:
                pass

    @classmethod
    def _get_content_tag(cls, tag):
        mapping = dict()
        cls.__find_content_tag(tag, mapping)
        s_list = sorted(mapping.iteritems(), key=lambda k: k[1], reverse=True)
        if len(s_list) == 0:
            return None, 0
        item = s_list[0]
        tag = item[0]
        length = item[1]
        return tag, length

    @classmethod
    def __find_content_tag(cls, tag, mapping):
        if isinstance(tag, Tag):
            mapping[tag] = len(tag.contents)
            for child in tag.children:
                cls.__find_content_tag(child, mapping)

    @staticmethod
    def __get_img_src(tag):
        img_url_name = ["src", "alt-src", "data-src"]
        for name in img_url_name:
            url = tag.get(name, "").strip()
            if url.startswith("http"):
                return url
        return ""

    @staticmethod
    def _show(content):
        for item in content:
            for key, value in item.items():
                print("%s: %s" % (key, value))


class BaseExtractor(object):

    def __init__(self, document):
        self.doc = document
        self.html = self.clean(self.doc)
        self.soup = BeautifulSoup(self.html, "lxml")

    @staticmethod
    def clean(doc):
        return doc

    def extract_title(self):
        return ""

    def extract_post_date(self):
        return ""

    def extract_post_user(self):
        return ""

    def extract_content(self):
        raise NotImplementedError

    def __call__(self):
        title = self.extract_title()
        post_date = self.extract_post_date()
        post_user = self.extract_post_user()
        content = self.extract_content()
        return title, post_date, post_user, content

    def find_content_tag(self, *args, **kwargs):
        if args or kwargs:
            tag = self.soup.find(*args, **kwargs)
        else:
            tag = self.soup.body
        mapping = dict()

        def _find_content_tag(t):
            if isinstance(t, NavigableString):
                mapping[t] = 1
            elif isinstance(t, Tag):
                mapping[t] = len(t.contents)
                for child in t.children:
                    _find_content_tag(child)

        _find_content_tag(tag)
        sorted_mapping = sorted(mapping.iteritems(),
                                key=lambda k: k[1],
                                reverse=True)
        return None if not sorted_mapping else sorted_mapping[0][0]

    @staticmethod
    def remove_tag_name(string, name):
        p = re.compile("<{tag}[^>]*>|</{tag}>".format(tag=name))
        return re.sub(p, "", string)

    @staticmethod
    def get_img_src(tag):
        img_url_name = ["src", "alt-src", "data-src"]
        for name in img_url_name:
            url = tag.get(name, "").strip()
            if url.startswith("http"):
                return url
        return ""

    @staticmethod
    def get_content_item(key, value):
        keys = {"text": "text", "image": "img"}
        assert key in keys
        return {keys[key]: value.strip()}

    @staticmethod
    def show(content):
        for item in content:
            for key, value in item.items():
                print("%s: %s" % (key, value))

    def get_tag_text(self, *args, **kwargs):
        tag = self.soup.find(*args, **kwargs)
        return tag.get_text().strip() if tag else ""


class GeneralExtractor(BaseExtractor):

    @staticmethod
    def clean(doc):
        allow_tags = ("b", "blod", "big", "em", "font", "h1", "h2", "h3", "h4",
                      "h5", "h6", "i", "italic", "small", "strike", "sub",
                      "a", "p", "strong", "div", "img", "tt", "u", "html",
                      "meta", "body", "head", "br", "sup")
        encoding = "utf-8"
        cleaner = Cleaner(scripts=True, javascript=True, comments=True,
                          style=True, links=True, meta=False,
                          add_nofollow=False, page_structure=False,
                          processing_instructions=True, embedded=False,
                          frames=False, forms=False, annoying_tags=False,
                          remove_tags=None, remove_unknown_tags=False,
                          safe_attrs_only=False, allow_tags=allow_tags)
        parser = html.HTMLParser(encoding=encoding, remove_comments=True,
                                 remove_blank_text=True)
        document = html.document_fromstring(doc, parser=parser)
        document = cleaner.clean_html(document)
        return html.tostring(document, encoding=encoding)

    def extract_content(self):
        tag = self.find_content_tag()
        content = list()

        def _extract_content(t):
            for child in t.children:
                if isinstance(child, NavigableString):
                    string = unicode(child).strip()
                    if string:
                        content.append(self.get_content_item("text", string))
                elif isinstance(child, Tag):
                    if child.name == "img":
                        src = self.get_img_src(child)
                        if src:
                            content.append(self.get_content_item("image", src))
                    elif child.name == "div" or child.img or child.br:
                        _extract_content(child)
                    elif child.get_text().strip():
                        string = str(child)
                        if child.name == "p":
                            string = self.remove_tag_name(string, "p")
                        content.append(self.get_content_item("text", string))
                else:
                    pass

        _extract_content(tag)
        return content


class RegularExtractor(GeneralExtractor):

    def extract_content(self):
        tag = self.find_content_tag()
        content = list()

        def _extract_content(t):
            for child in t.children:
                if isinstance(child, NavigableString):
                    string = unicode(child).strip()
                    if string:
                        content.append(self.get_content_item("text", string))
                elif isinstance(child, Tag):
                    if child.name == "img":
                        src = self.get_img_src(child)
                        if src:
                            content.append(self.get_content_item("image", src))
                    elif child.img:
                        _extract_content(child)
                    elif child.get_text().strip():
                        string = str(child)
                        if child.name == "p":
                            string = self.remove_tag_name(string, "p")
                        content.append(self.get_content_item("text", string))
                    else:
                        pass
                else:
                    pass
        _extract_content(tag)
        return content

