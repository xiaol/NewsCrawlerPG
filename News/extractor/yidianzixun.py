# coding: utf-8

from bs4 import NavigableString, Tag
from News.constans.yidianzixun import OUTER
from News.extractor import NewsExtractor
from News.monitor import monitor


class YiDianZiXunExtractor(NewsExtractor):

    outer = OUTER

    def extract(self):
        if "content-bd" in self.html:
            return self._extract_inner()
        elif self.__is_outer():
            return self._extract_outer()
        else:
            return self._not_support_now()

    def __is_outer(self):
        if "yidian-content" in self.html:
            return True
        for string in self.outer:
            if string in self.url:
                return True
        return False

    @monitor(error=2)
    def _extract_inner(self):
        tag = self.soup.find("div", class_="content-bd")
        self._remove_tag(tag, "p", class_="copyright")
        self._remove_tag(tag, "div", class_="report")
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count

    @monitor(error=2)
    def _extract_outer(self):
        tag = self.soup.find("div", class_="TRS_Editor") \
              or self.soup.find("div", class_="yidian-content") \
              or self.soup.find("div", class_="article-content")
        self._remove_tag(tag, "div", class_="video-area")
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count

    @monitor(error=1)
    def _not_support_now(self):
        return [], 0

