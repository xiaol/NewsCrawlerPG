# coding: utf-8

SPIDER_NAME = "spider:news:wechat"
CRAWL_SOURCE = u"微信公众号"
START_URL_PREFIX = "http://weixin.sogou.com"


ID_NAME_MAPPING = {
    "0": u"今日焦点",
    "1": u"热门专题",
    "2": u"重口味",
    "3": u"贵圈乱不乱",
    "4": u"反正我信了",
    "5": "Take ground gas",
    "6": u"直男常备",
    "8": u"股往金来",
    "9": u"科学嗨起来",
    "10": u"高逼格get√",
    "11": u"追剧看片schedule",
    "12": u"音痴恐惧症",
    "13": u"萌师强化班",
    "14": u"X星人沦陷区",
    "15": u"谷歌今日焦点",
    "16": u"外媒观光团",
}

SOURCES = [
    {"oid": "xxxjiji", "name": u"我们爱讲冷笑话", "channel_id": "2"},
    {"oid": "mhxy88", "name": u"我们爱讲冷笑话", "channel_id": "2"},
    {"oid": "n0451sj", "name": u"世界未解之谜", "channel_id": "2"},
    {"oid": "wjzm69", "name": u"世界全球未解之谜", "channel_id": "2"},

    {"oid": "gossipmaker", "name": u"关爱八卦成长协会", "channel_id": "3"},

    {"oid": "dandureading", "name": u"单读", "channel_id": "10"},

    {"oid": "loveetdog", "name": u"汪星人", "channel_id": "14"},
    {"oid": "wangxinggou", "name": u"我是汪星人", "channel_id": "14"},
    {"oid": "mengchongmeng", "name": u"萌宠萌", "channel_id": "14"},
    {"oid": "petxiu", "name": u"萌宠秀", "channel_id": "14"},
    {"oid": "daaimaomikong", "name": u"大爱猫咪控", "channel_id": "14"},

    {"oid": "iwaimei", "name": u"外媒看天朝", "channel_id": "16"},
]
