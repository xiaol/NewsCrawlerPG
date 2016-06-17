# coding: utf-8

from News.extractor import NewsExtractor, GeneralExtractor, find_content_tag
from News.monitor import monitor


class News163Extractor(NewsExtractor):

    @monitor(error=2)
    def extract(self):
        tag = self.soup.body
        result = self._extract(tag)
        contents, count = self.g_returns(result)
        return contents, count


class G3News163Extractor(GeneralExtractor):

    def extract_content(self, param={'method': 'find_all', 'params': {'name': 'div'}},
                        clean_param_list=None,
                        clean_content_before_param=None,
                        clean_content_after_param=None,
                        default_score_content=None,):
        content = list()
        if param is None:
            tag = find_content_tag(self.soup.body)
        else:
            tag = self.exact_find_tag(self.soup, param)
            if tag is None:
                tag = find_content_tag(self.soup.body)
        if tag is None:
            return content
        if clean_content_before_param is not None:
            self.content_tag_clean_before(tag, clean_content_before_param)
        if clean_content_after_param is not None:
            self.content_tag_clean_after(tag, clean_content_after_param)
        if clean_param_list is not None:
            self.content_tag_clean(tag, clean_param_list)
        self.parse_content_tag(tag, content)
        return self.clean_content(content)