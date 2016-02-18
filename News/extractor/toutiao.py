# coding: utf-8

from News.constans.toutiao import DOMAIN
from News.constans.toutiao import OUTER
from News.extractor import NewsExtractor
from News.monitor import monitor


class TouTiaoExtractor(NewsExtractor):

    outer = OUTER

    def extract(self):
        if DOMAIN in self.url:
            return self._extract_inner()
        elif self.__is_outer():
            return self._extract_outer()
        else:
            return self._not_support_now()

    def __is_outer(self):
        if "TouTiaoBar" in self.html:
            return True
        for string in self.outer:
            if string in self.url:
                return True
        return False

    @monitor(error=2)
    def _extract_inner(self):
        tag = self.soup.find("div", class_="article-content")
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count

    @monitor(error=2)
    def _extract_outer(self):
        tag = self.soup.find("div", class_="article-content") \
              or self.soup.find("article") \
              or self.soup.find("div", id="gallery") \
              or self.soup.find("div", class_="article-body") \
              or self.soup.find("div", id="_j_content")
        self._remove_tag(tag, "div", id="TouTiaoBar")
        self._remove_tag(tag, "header")
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count

    @monitor(error=1)
    def _not_support_now(self):
        return [], 0



