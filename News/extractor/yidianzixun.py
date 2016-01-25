from bs4 import NavigableString, Tag
from News.extractor import NewsExtractor


class YiDianZiXunExtractor(NewsExtractor):

    def extract(self):
        result = list()
        content = self.soup.find("div", class_="TRS_Editor")
        if not content:
            content = self.soup.find("div", id="yidian-content")
        if not content:
            content = self.soup.find("div", class_="content-bd")
        if not content:
            return [], 0
        for child in content.contents:
            if isinstance(child, NavigableString):
                string = unicode(child)
                if string and string.strip():
                    result.append({"text": string.strip()})
            elif isinstance(child, Tag):
                ignore = child.get("class", [])
                if child.name == "img":
                    src = child.get("src") or child.get("alt_src")
                    result.append({"img": src})
                elif child.img:
                    src = child.img.get("src") or child.img.get("alt_src")
                    result.append({"img": src})
                else:
                    classes = ["copyright", "report", "video-area"]
                    for c in classes:
                        if c in ignore: break
                    else:
                        result.append({"text": child.get_text()})
            else:
                pass
        contents, count = self.g_returns(content)
        return contents, count








