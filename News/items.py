# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class NewsItem(Item):
    title = Field()     # 标题 str
    tags = Field()      # 关键字 ['str',...]
    summary = Field()   # 摘要 str
    publish_time = Field()  # 发布时间 str
    content = Field()   # 内容 ['img': '', 'text': '', 'video': '',...]
    province = Field()  # 省 str
    city = Field()  # 市 str
    district = Field()  # 区/县 str
    love = Field()  # 喜爱 int
    up = Field()    # 顶 int
    down = Field()  # 踩 int
    image_number = Field()  # 图片数 int

    docid = Field()     # 网站内部唯一标识
    channel = Field()   # 频道 str
    category = Field()  # 分类 str
    crawl_url = Field()     # 抓取网址 str
    original_url = Field()  # 源网址 str
    crawl_source = Field()  # 抓取地址 str
    original_source = Field()   # 源地址 str

    key = Field()   # redis key, base64 for crawl_url
    start_url = Field()  # start url, record to get channel info in pipeline


class CommentItem(Item):
    comment_id = Field()
    content = Field()
    nickname = Field()
    love = Field()
    create_time = Field()
    profile = Field()
    docid = Field()
    pid = Field()

