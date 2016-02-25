# coding: utf-8
import re
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
        if not tag:
            return result
        children = []
        for child in tag.children:
            if isinstance(child, Tag):
                children.append(child)
        if len(children) <= length:
            tag = children[0]
        for child in tag.children:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                if child.name == "img":
                    result.append({"img": cls.__get_img_src(child)})
                elif child.img:
                    result.append({"img": cls.__get_img_src(child.img)})
                else:
                    result.append({"text": child.get_text().strip()})
            else:
                pass
        return result

    @staticmethod
    def __get_img_src(tag):
        return tag.get("src") or tag.get("alt-src") or tag.get("data-src")

    @staticmethod
    def _show(content):
        for item in content:
            for key, value in item.items():
                print("%s: %s" % (key, value))




