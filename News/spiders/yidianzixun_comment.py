# coding: utf-8
from importlib import import_module
from time import strftime
import json
import re
from scrapy import Request
from bs4 import BeautifulSoup

from News.distributed import RedisSpider
from News.items import CommentItem
from News.constans.yidianzixun import COMMENT_SPIDER_NAME, SPIDER_NAME


class YidianzixunCommentsSpider(RedisSpider):

    name = COMMENT_SPIDER_NAME
    base_url = 'http://www.yidianzixun.com/api/q/?path=contents/comments&version=999999&docid={docid}&count={count_per_page}'
    crawl_source = SPIDER_NAME
    default_comment_count = 100

    def parse(self, response):
        json_data = response.body
        dict_data = json.loads(json_data)
        if not dict_data['comments']:
            return
        comments = dict_data['comments']
        if 'total' in dict_data and dict_data['total'] == 0:
            return
        docid = dict_data['docid']
        fk_docid = response.meta.get('docid', response.url)
        for comment in comments:
            yield self._parse_comment(comment, fk_docid)
        last_comment_id = comment['comment_id']
        yield self.g_comment_request(docid=docid, fk_docid=fk_docid, last_comment_id=last_comment_id, count_per_page=100)



    def g_comment_request(self, docid, fk_docid, last_comment_id='', count_per_page=100):
        url = self.base_url.format(docid=docid, count_per_page=count_per_page)
        if last_comment_id:
            url += '&last_comment_id=%s' % last_comment_id
        return Request(
            url=url,
            callback=self.parse,
            meta={'docid': fk_docid}
        )

    def _parse_comment(self, comment, fk_docid):
        item = CommentItem()
        item['comment_id'] = comment['comment_id']
        item['nickname'] = comment['nickname']
        item['love'] = comment['like']
        item['create_time'] = comment['createAt']
        item['profile'] = comment['profile']
        item['docid'] = fk_docid
        if comment['comment'].strip():
            item['content'] = comment['comment']
            return item
        else:
            return None