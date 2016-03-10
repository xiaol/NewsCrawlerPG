# coding: utf-8

from datetime import datetime
from News.extractor import GeneralExtractor


class WechatExtractor(GeneralExtractor):

    def extract_title(self):
        return self.get_tag_text(id="activity-name")

    def extract_post_date(self):
        dt = self.get_tag_text(id="post-date")
        now = datetime.now()
        return dt + now.strftime(" %H:%M:%S") if dt else ""

    def extract_post_user(self):
        return self.get_tag_text(id="post-user")

    def find_content_tag(self):
        return self.soup.find(id="js_content")












