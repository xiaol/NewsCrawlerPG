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

    image_list = Field()    # 新闻 meta 图片列表， 只为向下兼容

    key = Field()   # redis key, base64 for crawl_url
    start_url = Field()  # start url, record to get channel info in pipeline


def get_default_news(title="", tags=None, summary="", publish_time="",
                     content=None, province=None, city=None, district=None,
                     love=0, up=0, down=0, image_number=0, docid="",
                     channel="", category="", crawl_url="", original_url="",
                     crawl_source="", original_source="", image_list=None,
                     key="", start_url=""):
    news = NewsItem()
    news["title"] = title
    if tags is None: news["tags"] = list()
    news["summary"] = summary
    news["publish_time"] = publish_time
    if content is None:
        news["content"] = list()
    news["province"] = province
    news["city"] = city
    news["district"] = district
    news["love"] = love
    news["up"] = up
    news["down"] = down
    news["image_number"] = image_number
    news["docid"] = docid
    news["channel"] = channel
    news["category"] = category
    news["crawl_url"] = crawl_url
    news["original_url"] = original_url
    news["crawl_source"] = crawl_source
    news["original_source"] = original_source
    if image_list is None: news["image_list"] = list()
    news["key"] = key
    news["start_url"] = start_url
    return news


class CommentItem(Item):
    comment_id = Field()
    content = Field()
    nickname = Field()
    love = Field()
    create_time = Field()
    profile = Field()
    docid = Field()
    pid = Field()

