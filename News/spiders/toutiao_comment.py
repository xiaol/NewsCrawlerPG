# coding: utf-8
from importlib import import_module
from time import strftime
import json
import re
from scrapy import Request
from bs4 import BeautifulSoup

from News.distributed import RedisSpider
from News.items import CommentItem
from News.utils.util import str_from_timestamp
from News.constans.toutiao import COMMENT_SPIDER_NAME


class ToutiaoCommentsSpider(RedisSpider):

    name = COMMENT_SPIDER_NAME
    base_url = 'http://toutiao.com/group/{group_id}/comments/?count={count_per_page}&offset={offset_count}&format=json'
    crawl_source = u'今日头条'
    default_comment_count = 100
    pattern_docid = re.compile('(/group/[0-9]+/)')

    def parse(self, response):
        json_data = response.body
        dict_data = json.loads(json_data)
        if not dict_data['data']:
            return
        comments = dict_data['data']['comments']
        total_count = dict_data['data']['comment_pagination']['total_count']
        page_count = dict_data['data']['comment_pagination']['count']
        if total_count == 0:
            return
        docid_match = self.pattern_docid.search(response.url)
        if not docid_match:
            return
        docid = docid_match.group(0).split('/')[-2]
        offset = int(dict_data['data']['comment_pagination']['offset']) + page_count
        for comment in comments:
            yield self._parse_comment(comment, response)
        if offset < total_count:
            yield self.g_comment_request(docid=docid, offset=offset)

    def g_comment_request(self, docid, offset, count_per_page=100):
        url = self.base_url.format(group_id=docid, count_per_page=count_per_page, offset_count=offset)
        return Request(
            url=url,
            callback=self.parse,
            meta={'docid': docid, 'offset': offset}
        )

    def _parse_comment(self, comment, docid):
        item = CommentItem()
        item['comment_id'] = comment['id']
        item['nickname'] = comment['user_name']
        item['love'] = comment['digg_count']
        item['create_time'] = str_from_timestamp(comment['create_time'])
        item['profile'] = comment['user_profile_image_url']
        item['docid'] = docid
        if comment['text'].strip():
            item['content'] = comment['text']
            return item
        else:
            return None