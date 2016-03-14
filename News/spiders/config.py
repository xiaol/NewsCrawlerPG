# coding: utf-8


configs = [
    {
        "allowed_domains": ["news.sina.com.cn"],
        "start_urls": ["http://news.sina.com.cn/society/"],
        "rule": {
            "follow_allow": [r"^http://news\.sina\.com\.cn/[a-z0-9A-Z]\w*/$"],
            "follow_deny": [],
            "parse_allow": [r"^http://\S*news\.sina\.com\.cn/\S*\d{4}-\d{2}-\d{2}/\S*\.shtml$"],
            "parse_deny": ["http://\S*news.sina.com.cn/\S*video\d{4}-\d{2}-\d{2}/\S*\.shtml$"],
        },
        "title_param": {"name": None, "attrs": {"id": "artibodyTitle"}},
        "post_date_param": {"name": "meta", "attrs": {"name": "weibo: article:create_at"}},
        "post_user_param": {"name": "meta", "attrs": {"name": "mediaid"}},
        "summary_param": {"name": "meta", "attrs": {"name": "description"}},
        "content_param": {"name": None, "attrs": {}},
        "db": "mongodb",
        "channel_id": "",
        "crawl_source": "新浪新闻",
        "description": "新浪新闻抓取配置文件",
        "online": False,
    },
    {
        "allowed_domains": ["www.waou.com.mo"],
        "start_urls": ["http://www.waou.com.mo/main.php"],
        "rule": {
            "follow_allow": [r"^http://www\.waou\.com\.mo/news_[a-i]/$"],
            "follow_deny": [],
            "parse_allow": [r"^http://www\.waou\.com\.mo/news_[a-i]/shownews\.php\?lang=cn&id=[0-9]*",
                            r"^http://www\.waou\.com\.mo/news_[a-i]/shownews\.php\?id=[0-9]*&lang=cn"],
            "parse_deny": [],
        },
        "title_param": {"name": "h1", "attrs": {}},
        "post_date_param": {"name": "div", "attrs": {"class": "mc_hits"}},
        "post_user_param": {"name": None, "attrs": {}},
        "summary_param": {"name": None, "attrs": {}},
        "content_param": {"name": None, "attrs": {}},
        "db": "mongodb",
        "channel_id": "",
        "crawl_source": "新华澳报",
        "description": "新华澳报抓取配置文件",
        "online": True,
    },

]


