# coding: utf-8

from datetime import datetime
from News.extractor import GeneralExtractor


class WechatExtractor(GeneralExtractor):

    title_param = {"args": list(), "kwargs": dict(id="activity-name")}
    post_date_param = {"args": list(), "kwargs": dict(id="post-date")}
    post_user_param = {"args": list(), "kwargs": dict(id="post-user")}
    content_param = {"args": list(), "kwargs": dict(id="js_content")}
    #
    # def extract_title(self):
    #     return self.get_tag_text(id="activity-name")
    #
    # def extract_post_date(self):
    #     dt = self.get_tag_text(id="post-date")
    #     now = datetime.now()
    #     return dt + now.strftime(" %H:%M:%S") if dt else ""
    #
    # def extract_post_user(self):
    #     return self.get_tag_text(id="post-user")
    #
    # def find_content_tag(self):
    #     return self.soup.find(id="js_content")

    def clean_post_date(self, string):
        now = datetime.now()
        return string + now.strftime(" %H:%M:%S") if string else ""












