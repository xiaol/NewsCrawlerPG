# coding: utf-8


import tornado.ioloop
import tornado.web

from News.test.extractor import test_extractor


class ExtractorHandler(tornado.web.RequestHandler):

    def post(self):
        key = self.get_argument("key")
        url = self.get_argument("url")
        title, post_date, post_user, content = test_extractor(key, url)
        results = {
            "title": title,
            "post_date": post_date,
            "post_user": post_user,
            "content": content,
        }
        self.write(results)


def make_app():
    return tornado.web.Application([
        (r"/", ExtractorHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



