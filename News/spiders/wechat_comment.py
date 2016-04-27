# coding: utf-8
from importlib import import_module
from time import strftime
import json
import re
from scrapy import Request
from bs4 import BeautifulSoup

from News.distributed import RedisSpider
from News.items import CommentItem
from News.constans.wechat import COMMENT_SPIDER_NAME, SPIDER_NAME
from News.utils.util import str_from_timestamp

class WechatCommentsSpider(RedisSpider):

    name = COMMENT_SPIDER_NAME
    # base_url = 'http://www.yidianzixun.com/api/q/?path=contents/comments&version=999999&docid={docid}&count={count_per_page}'
    crawl_source = SPIDER_NAME
    default_comment_count = 100

    def parse(self, response):
        json_data = response.body
        dict_data = json.loads(json_data)
        if 'comment' not in dict_data or not dict_data['comment']:
            return
        comments = dict_data['comment']
        fk_docid = response.meta.get('docid', response.url)
        for comment in comments:
            yield self._parse_comment(comment, fk_docid)
        # last_comment_id = comment['comment_id']
        # yield self.g_comment_request(docid=docid, fk_docid=fk_docid, last_comment_id=last_comment_id, count_per_page=100)



    # def g_comment_request(self, docid, fk_docid, last_comment_id='', count_per_page=100):
    #     url = self.base_url.format(docid=docid, count_per_page=count_per_page)
    #     if last_comment_id:
    #         url += '&last_comment_id=%s' % last_comment_id
    #     return Request(
    #         url=url,
    #         callback=self.parse,
    #         meta={'docid': fk_docid}
    #     )

    def _parse_comment(self, comment, fk_docid):
        item = CommentItem()
        item['comment_id'] = comment['content_id']
        item['nickname'] = comment['nick_name']
        item['love'] = int(comment['like_num'])
        item['create_time'] = str_from_timestamp(comment['create_time'])
        item['profile'] = comment['logo_url']
        item['docid'] = fk_docid
        if comment['content'].strip():
            item['content'] = comment['content']
            return item
        else:
            return None