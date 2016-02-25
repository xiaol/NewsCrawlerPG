# coding: utf-8

from datetime import datetime
from News.extractor import NewsExtractor
from News.monitor import monitor


class WechatExtractor(NewsExtractor):

    def extract(self):
        title = self.__extract_title()
        publish_time = self.__extract_post_date()
        publish_user = self.__extract_post_user()
        content, count = self.__extract_content()
        self.news["title"] = title
        self.news["publish_time"] = publish_time
        self.news["original_source"] = publish_user
        self.news["original_url"] = self.news["crawl_url"]
        return content, count

    def __extract_title(self):
        tag = self.soup.find(id="activity-name")
        if tag:
            return tag.get_text().strip()
        else:
            return ""

    def __extract_post_date(self):
        tag = self.soup.find(id="post-date")
        now = datetime.now()
        if tag:
            return tag.get_text().strip() + " " + now.strftime("%H:%M:%S")
        else:
            return ""

    def __extract_post_user(self):
        tag = self.soup.find(id="post-user")
        if tag:
            return tag.get_text().strip()
        else:
            return ""

    @monitor(error=2)
    def __extract_content(self):
        tag = self.soup.find(id="js_content")
        result = self._extract_regular(tag, length=3)
        contents, count = self.g_returns(result)
        return contents, count















