# coding: utf-8

SPIDER_NAME = "spider:news:wechat"
COMMENT_SPIDER_NAME = "spider:news:comment:wechat"
CRAWL_SOURCE = u"微信公众号"

# SOURCES = [
#     # {"oid": "xxxjiji", "name": u"我们爱讲冷笑话", "channel_id": "2"},
#     # {"oid": "mhxy88", "name": u"我们爱讲冷笑话", "channel_id": "2"},
#     # {"oid": "n0451sj", "name": u"世界未解之谜", "channel_id": "2"},
#     # {"oid": "wjzm69", "name": u"世界全球未解之谜", "channel_id": "2"},
#     #
#     # {"oid": "gossipmaker", "name": u"关爱八卦成长协会", "channel_id": "3"},
#     #
#     # {"oid": "dandureading", "name": u"单读", "channel_id": "10"},
#     #
#     # {"oid": "loveetdog", "name": u"汪星人", "channel_id": "14"},
#     # {"oid": "wangxinggou", "name": u"我是汪星人", "channel_id": "14"},
#     # {"oid": "mengchongmeng", "name": u"萌宠萌", "channel_id": "14"},
#     # {"oid": "petxiu", "name": u"萌宠秀", "channel_id": "14"},
#     # {"oid": "daaimaomikong", "name": u"大爱猫咪控", "channel_id": "14"},
#     #
#     {"oid": "iwaimei", "name": u"外媒看天朝", "channel_id": "16"},
# ]

CATEGORIES = [
    {
        "oid": "iwaimei",
        "name": u"外媒看天朝",
        "channel_id": 29,
        "frequency": 60*5,
        "description": u"外媒如何看中国？不用翻墙，这里都有。",
        "image": "",
        "url": "",
    },
    {
        "oid": "geekpark",
        "name": u"极客公园",
        "channel_id": 4,
        "frequency": 60*5,
        "description": u"科技创新者的大本营。汇聚优秀的产品报道、评测视频和高质量的线下活动。",
        "image": "",
        "url": "",
    },
]
