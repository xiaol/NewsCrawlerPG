# coding: utf-8

"""
解析与打分 web 服务
"""
import json
import os
import tornado.ioloop
import tornado.web
from redis import Redis
from tornado.web import RequestHandler

from News.service import extract_service, score_service, GeneralExtractor
from News.utils.cache import Cache


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


class ExtractByHTMLHandler(RequestHandler):
    def post(self, *args, **kwargs):
        html = self.get_argument('content_html')
        print html
        extractor = GeneralExtractor(html)
        title, post_date, post_user, summary, content = extractor()
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


class ItemHandler(RequestHandler):

    def get(self, *args, **kwargs):
        r = Redis()
        new_keys = r.keys('news*')
        new_keys = new_keys[:10]
        news = [r.hgetall(i) for i in new_keys]
        html_code_list = list()
        for i in news:
            html = ''
            html += '<center><h2>' + i['title'] + '</h2></center>'
            html += '<p>' + i['pub_time'] + '</p>'
            html += '<p>' + i['pub_name'] + '</p>'
            content = json.loads(i['content'])
            for j in content:
                if 'txt' in j:
                    html += '<p>&nbsp&nbsp&nbsp&nbsp&nbsp' + j['txt'].encode('utf8') + '</p>'
                elif 'img' in j:
                    html += '<center><img src="' + j['img'].encode('utf8') + '"></center>'
            html_code_list.append(html)
        self.render('item.html', data=html_code_list)


def make_app():
    settings = {
        "template_path": "web",
        "static_path": os.path.join(os.path.dirname(__file__), "web"),
    }
    return tornado.web.Application([
        (r"/", ExtractorHandler),
        (r'/htmlextract', ExtractByHTMLHandler),
        (r"/score", ScoreHandler),
        (r'/item', ItemHandler)
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()



