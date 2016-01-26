# coding: utf-8

from bs4 import BeautifulSoup, Comment, Tag, NavigableString


class NewsExtractor(object):

    HARD_TAGS = ["<strong>", "</strong>", "<em>", "</em>", "<br>"]
    TAGS = ["script", "link"]

    def __init__(self, html, url=None, hard_tags=None, tags=None, news=None):
        self.html = html
        self.cleaned_html = html
        self.url = url
        self.hard_tags = hard_tags if hard_tags is not None else self.HARD_TAGS
        self.tags = tags if hard_tags is not None else self.TAGS
        self._hard_remove_tags()
        self.soup = BeautifulSoup(self.cleaned_html, "lxml")
        self._remove_comments()
        self._remove_tags()
        self.news = news

    def _hard_remove_tags(self):
        for tag in self.hard_tags:
            self.cleaned_html = self.cleaned_html.replace(tag, "")

    def _remove_comments(self):
        comments = self.soup.find_all(text=lambda text: isinstance(text, Comment))
        [comment.extract() for comment in comments]

    def _remove_tags(self):
        [tag.extract() for tag in self.soup.find_all(self.tags)]

    @staticmethod
    def _remove_tag(tag, name, **kwargs):
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

    @staticmethod
    def _extract(tag):
        result = list()
        if not tag: return result
        for child in tag.descendants:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                if child.name == "img":
                    result.append(
                            {"img": child.get("src") or child.get("alt-src")}
                    )
            else:
                pass
        return result




