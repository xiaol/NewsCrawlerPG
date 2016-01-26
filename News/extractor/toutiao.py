# coding: utf-8

from News.constans.toutiao import DOMAIN
from News.extractor import NewsExtractor
from News.monitor import monitor


class TouTiaoExtractor(NewsExtractor):

    def extract(self):
        if DOMAIN in self.url:
            return self._extract_inner()
        elif "TouTiaoBar" in self.html:
            return self._extract_outer()
        else:
            return self._not_support_now()

    @monitor(error=2)
    def _extract_inner(self):
        tag = self.soup.find("div", class_="article-content")
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count

    @monitor(error=2)
    def _extract_outer(self):
        tag = self.soup.find("article") or self.soup.find("div", id="gallery")
        self._remove_tag(tag, "div", id="TouTiaoBar")
        self._remove_tag(tag, "header")
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count

    @monitor(error=1)
    def _not_support_now(self):
        return [], 0



