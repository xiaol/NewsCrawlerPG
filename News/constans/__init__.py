# coding: utf-8

CACHE_SOURCE_KEY = "spider_source:hashtable"
NEWS_STORE_API = "http://api.deeporiginalx.com/bdp/spider/pipeline/task/{key}"
COMMENT_STORE_API = "http://api.deeporiginalx.com/bdp/news/comment/ydzx"

CHANNELS_MAP = {
    1: {"name": u"热点", "online": 1},
    2: {"name": u"社会", "online": 1},
    3: {"name": u"娱乐", "online": 1},
    4: {"name": u"科技", "online": 1},
    5: {"name": u"汽车", "online": 1},
    6: {"name": u"体育", "online": 1},
    7: {"name": u"财经", "online": 1},
    8: {"name": u"军事", "online": 1},
    9: {"name": u"国际", "online": 1},
    10: {"name": u"时尚", "online": 1},
    11: {"name": u"游戏", "online": 1},
    12: {"name": u"旅游", "online": 1},
    13: {"name": u"历史", "online": 1},
    14: {"name": u"探索", "online": 1},
    15: {"name": u"美食", "online": 1},
    16: {"name": u"育儿", "online": 1},
    17: {"name": u"养生", "online": 1},
    18: {"name": u"故事", "online": 1},
    19: {"name": u"美文", "online": 1},
    20: {"name": u"股票", "online": 1},
    21: {"name": u"搞笑", "online": 1},
    22: {"name": u"互联网", "online": 1},
    23: {"name": u"趣图", "online": 1},
    24: {"name": u"健康", "online": 1},
    25: {"name": u"科学", "online": 1},
    26: {"name": u"美女", "online": 1},
    27: {"name": u"杂志", "online": 0},
    28: {"name": u"本地", "online": 0},
    "0": {"name": u"今日焦点", "online": 1},    # 热点
    "1": {"name": u"热门专题", "online": 1},    # 精选
    "2": {"name": u"重口味", "online": 1},     # 重口味
    "3": {"name": u"贵圈乱不乱", "online": 1},   # 娱乐
    "4": {"name": u"反正我信了", "online": 1},   # 搞笑
    "5": {"name": "Take ground gas", "online": 1},  # 社会
    "6": {"name": u"直男常备", "online": 1},    # 体育
    "8": {"name": u"股往金来", "online": 1},    # 财经
    "9": {"name": u"科学嗨起来", "online": 1},   # 科技
    "10": {"name": u"高逼格get√", "online": 1},    # 时尚
    "11": {"name": u"追剧看片schedule", "online": 1},   # 影视
    "12": {"name": u"音痴恐惧症", "online": 1},  # 音乐
    "13": {"name": u"萌师强化班", "online": 1},  # 二次元
    "14": {"name": u"X星人沦陷区", "online": 1},  # 萌宠
    "15": {"name": u"谷歌今日焦点", "online": 1},  # 推荐
    "16": {"name": u"外媒观光团", "online": 1},  # 外媒
}

SPIDER_CONFIG_NAMES = [
    "News.constans.www_gq_com_cn",
    "News.constans.i_cri_cn",
    "News.constans.jandan_net",
    "News.constans.moviesoon_com",
    "News.constans.pansci_asia",
    "News.constans.www_adaymag_com",
    "News.constans.www_chinanews_com",
    "News.constans.www_ifeng_com",
    "News.constans.www_hexun_com",
    "News.constans.www_hjzlg_com",
    "News.constans.m_huanqiu_com",
    "News.constans.www_ifanr_com",
    "News.constans.jiecao_fm",
    "News.constans.www_jrj_com_cn",
    "News.constans.www_missevan_com",
    "News.constans.www_people_com_cn",
    "News.constans.www_pingwest_com",
    "News.constans.www_qianzhan_com",
    "News.constans.www_shejipi_com",
    "News.constans.sina_com_cn",
]
