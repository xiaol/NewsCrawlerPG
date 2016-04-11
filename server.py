# coding: utf-8

"""
解析与打分 web 服务
"""

import os
import tornado.ioloop
import tornado.web
from tornado.web import RequestHandler

from News.service import extract_service, score_service


class ExtractorHandler(RequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        key = self.get_argument("key")
        url = self.get_argument("url")
        title, post_date, post_user, summary, content = extract_service(key, url)
        results = {
            "title": title,
            "post_date": post_date,
            "post_user": post_user,
            "summary": summary,
            "content": content,
        }
        self.write(results)


class ScoreHandler(RequestHandler):

    def get(self):
        self.render("score.html")

    def post(self, *args, **kwargs):
        url = self.get_argument("url")
        data = score_service(url)
        results = {
            "data": data,
        }
        self.write(results)


def make_app():
    settings = {
        "template_path": "web",
        "static_path": os.path.join(os.path.dirname(__file__), "web"),
    }
    return tornado.web.Application([
        (r"/", ExtractorHandler),
        (r"/score", ScoreHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



