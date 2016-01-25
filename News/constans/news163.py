# coding: utf-8


SPIDER_NAME = "spider:news163"
ARTICLE_URL_TEMPLATE = "http://j.news.163.com/hy/doc.s?" \
                       "info=2&type=10&hash=&docid={docid}"
COMMENT_URL_TEMPLATE = "http://comment.news.163.com/api/v1" \
                       "/products/a2869674571f77b5a0867c3d71db5856/" \
                       "threads/{docid}/comments/newList?" \
                       "offset={offset}&limit=30"
DOMAIN = "http://j.news.163.com"
