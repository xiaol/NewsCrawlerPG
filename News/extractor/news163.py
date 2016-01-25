from bs4 import NavigableString, Tag
from News.extractor import NewsExtractor


class News163Extractor(NewsExtractor):

    def extract(self):
        result = list()
        tags = [child for child in self.soup.body.descendants]
        for tag in tags:
            if isinstance(tag, NavigableString):
                string = unicode(tag)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(tag, Tag):
                if tag.name == "img":
                    result.append({"img": tag.get("src")})
            else:
                pass
        contents, count = self.g_returns(result)
        return contents, count



