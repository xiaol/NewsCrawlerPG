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
from News.constans.news163 import COMMENT_SPIDER_NAME, SPIDER_NAME, COMMENT_URL_TEMPLATE


class News163CommentsSpider(RedisSpider):
    name = COMMENT_SPIDER_NAME
    crawl_source = SPIDER_NAME
    default_comment_count = 40
    pattern_docid = re.compile('(/threads/[\w]+/)')

    def parse(self, response):
        json_data = response.body
        # json_data = json_data[9:-3]

        dict_data = json.loads(json_data)
        count = dict_data['newListSize']
        if count == 0: return
        offset = response.meta.get('offset', 0)
        docid = self.pattern_docid.search(response.url).group(0).split('/')[-2]
        comment_ids = dict_data['commentIds']
        comments = dict_data['comments']
        if not comments:
            return
        for comment_id in comment_ids:
            comment_id = comment_id.split(',')[-1]
            if comment_id in comments:
                item = self._parse_comment(comments[comment_id], docid)
                if item is not None:
                    yield item
        if offset + len(comments) < count:
            yield self.g_comment_request(docid, offset + len(comments))

    def g_comment_request(self, docid, offset, count_per_page=default_comment_count):
        url = COMMENT_URL_TEMPLATE.format(docid=docid, count_per_page=count_per_page, offset=offset)
        return Request(
            url=url,
            callback=self.parse,
            meta={'docid': docid, 'offset': offset}
        )

    def _parse_comment(self, comment, docid):
        item = CommentItem()
        user = comment['user']
        item['comment_id'] = comment['commentId']
        item['nickname'] = user.get('nickname', '')
        item['love'] = comment['vote']
        item['create_time'] = comment['createTime']
        item['profile'] = user.get('avatar', '')
        item['docid'] = docid
        if comment['content'].strip():
            item['content'] = comment['content']
            return item
        else:
            return None
