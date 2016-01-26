# coding: utf-8

from News.extractor import NewsExtractor
from News.monitor import monitor


class News163Extractor(NewsExtractor):

    @monitor(error=2)
    def extract(self):
        tag = self.soup.body
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count



