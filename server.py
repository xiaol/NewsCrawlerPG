# coding: utf-8

import os
import tornado.ioloop
import tornado.web

from News.test.extractor import test_extractor


class ExtractorHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index.html")

    def post(self):
        key = self.get_argument("key")
        url = self.get_argument("url")
        title, post_date, post_user, summary, content = test_extractor(key, url)
        results = {
            "title": title,
            "post_date": post_date,
            "post_user": post_user,
            "summary": summary,
            "content": content,
        }
        self.write(results)


def make_app():
    settings = {
        "template_path": "web",
        "static_path": os.path.join(os.path.dirname(__file__), "web"),
    }
    return tornado.web.Application([
        (r"/", ExtractorHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



