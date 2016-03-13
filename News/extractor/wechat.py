# coding: utf-8

from datetime import datetime
from News.extractor import GeneralExtractor


class WechatExtractor(GeneralExtractor):

    title_param = {"name": None, "attrs": dict(id="activity-name")}
    post_date_param = {"name": None, "attrs": dict(id="post-date")}
    post_user_param = {"name": None, "attrs": dict(id="post-user")}
    content_param = {"name": None, "attrs": dict(id="js_content")}

    def clean_post_date(self, string):
        now = datetime.now()
        return string + now.strftime(" %H:%M:%S") if string else ""












