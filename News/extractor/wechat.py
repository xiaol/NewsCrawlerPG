# coding: utf-8

from News.extractor import GeneralExtractor


class WechatExtractor(GeneralExtractor):

    title_param = {"name": None, "attrs": dict(id="activity-name")}
    post_date_param = {"name": None, "attrs": dict(id="post-date")}
    post_user_param = {"name": None, "attrs": dict(id="post-user")}
    summary_param = {"name": None, "attrs": dict()}
    content_param = {"name": None, "attrs": dict(id="js_content")}












