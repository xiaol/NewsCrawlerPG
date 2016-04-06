## 资讯爬虫工程

### 一点资讯
url: http://www.yidianzixun.com/

### 今日头条
url: http://toutiao.com/

### 网易新闻
url: http://news.163.com/

### A Day Magazine
url: http://www.adaymag.com/

```python
CATEGORIES = {
    "WORLDPOST": {
        u"趣闻": ("http://www.adaymag.com/worldpost/fun/", None),
        u"奇闻": ("http://www.adaymag.com/worldpost/weird-news/", None),
        u"温情": ("http://www.adaymag.com/worldpost/heartwarming/", None),
        u"文化": ("http://www.adaymag.com/worldpost/culture/", None),
        u"科学": ("http://www.adaymag.com/worldpost/science/", None),
        u"女性议题": ("http://www.adaymag.com/worldpost/women/", None),
        u"同性议题": ("http://www.adaymag.com/worldpost/lgbt/", None),
        u"网络热话": ("http://www.adaymag.com/worldpost/viral/", None),
    },
    "LIFESTYLE": {
        u"职场": ("http://www.adaymag.com/lifestyle/career/", None),
        u"心理,占星": ("http://www.adaymag.com/lifestyle/%E5%BF%83%E7%90%86%E5%8D%A0%E6%98%9F/", None),
        u"旅游": ("http://www.adaymag.com/lifestyle/travel/", None),
        u"美食": ("http://www.adaymag.com/lifestyle/food/", None),
        u"好去处": ("http://www.adaymag.com/lifestyle/things-to-do/", None),
        u"宠物": ("http://www.adaymag.com/lifestyle/pet/", None),
        u"健康生活": ("http://www.adaymag.com/lifestyle/healthy-live/", None),
        u"两性关系": ("http://www.adaymag.com/lifestyle/love-relationship/", None),
    },
    "ART&DESIGN": {
        u"设计": ("http://www.adaymag.com/art-design/design/", None),
        u"建筑": ("http://www.adaymag.com/art-design/architecture/", None),
        u"艺术": ("http://www.adaymag.com/art-design/art/", None),
        u"摄影": ("http://www.adaymag.com/art-design/photography/", None),
    },
    "ENTERTAINMENT": {
        u"明星": ("http://www.adaymag.com/entertainment/celebrities/", None),
        u"音乐": ("http://www.adaymag.com/entertainment/music/", None),
        u"电影": ("http://www.adaymag.com/entertainment/movie/", None),
    },
    "FASHION": {
        # The Femin 女性时尚杂志
        # TRENDSFOLIO 男士时尚杂志
    },
}
```

### 海外网
url: http://www.haiwainet.cn/?v=1
废弃： http://world.haiwainet.cn/456832/

### 国际在线
url: http://i.cri.cn/

```python
CATEGORIES = {
    u"国际": ("http://i.cri.cn/world", None),
    u"国内": ("http://i.cri.cn/china", None),
    u"趣闻": ("http://i.cri.cn/popularnews", None),
    u"财经": ("http://i.cri.cn/finance", None),
    u"评论": ("http://i.cri.cn/opinion", None),
}
```

### 煎蛋
url: http://jandan.net/

```python
CATEGORIES = {
    u"科学": {
        u"走进科学": ("http://jandan.net/tag/%E8%B5%B0%E8%BF%9B%E7%A7%91%E5%AD%A6", None),
        u"无厘头研究": ("http://jandan.net/tag/%E6%97%A0%E5%8E%98%E5%A4%B4%E7%A0%94%E7%A9%B6", None),
        u"天文": ("http://jandan.net/tag/%E5%A4%A9%E6%96%87", None),
        u"NASA": ("http://jandan.net/tag/nasa", None),
        u"高科技": ("http://jandan.net/tag/%E9%AB%98%E7%A7%91%E6%8A%80", None),
        u"环保": ("http://jandan.net/tag/%E7%8E%AF%E4%BF%9D", None)
    },
    u"技术": {
        u"TECH": ("http://jandan.net/tag/tech", None),
        u"机器人": ("http://jandan.net/tag/%E6%9C%BA%E5%99%A8%E4%BA%BA", None),
        u"无人机": ("http://jandan.net/tag/%E6%97%A0%E4%BA%BA%E6%9C%BA", None),
        u"3D打印": ("http://jandan.net/tag/3D%E6%89%93%E5%8D%B0", None),
        u"数码产品": ("http://jandan.net/tag/%E6%95%B0%E7%A0%81%E4%BA%A7%E5%93%81", None),
        u"虚拟现实": ("http://jandan.net/tag/%E8%99%9A%E6%8B%9F%E7%8E%B0%E5%AE%9E", None),
    },
    u"极客": {
        u"GEEK": ("http://jandan.net/tag/GEEK", None),
        u"MEME": ("http://jandan.net/tag/MEME", None),
        u"QUORA": ("http://jandan.net/tag/quora", None),
        u"小学堂": ("http://jandan.net/tag/%E5%B0%8F%E5%AD%A6%E5%A0%82", None),
        u"创意产品": ("http://jandan.net/tag/%E5%88%9B%E6%84%8F%E4%BA%A7%E5%93%81", None),
        u"WHAT IF": ("http://jandan.net/tag/whatif", None),
    },
    u"脑洞": {
        u"DIY": ("http://jandan.net/tag/DIY", None),
        u"艺术": ("http://jandan.net/tag/%E8%89%BA%E6%9C%AF", None),
        u"设计": ("http://jandan.net/tag/%E8%AE%BE%E8%AE%A1", None),
        u"广告": ("http://jandan.net/tag/%E5%B9%BF%E5%91%8A", None),
        u"建筑": ("http://jandan.net/tag/%E5%BB%BA%E7%AD%91", None),
        u"摄影": ("http://jandan.net/tag/%E6%91%84%E5%BD%B1", None),
    },
    u"故事": {
        u"冷新闻": ("http://jandan.net/tag/%E5%86%B7%E6%96%B0%E9%97%BB", None),
        u"爷有钱": ("http://jandan.net/tag/%E7%88%B7%E6%9C%89%E9%92%B1", None),
        u"致富信息": ("http://jandan.net/tag/%E8%87%B4%E5%AF%8C%E4%BF%A1%E6%81%AF", None),
        u"安全警示": ("http://jandan.net/tag/%E5%AE%89%E5%85%A8%E8%AD%A6%E7%A4%BA", None),
        u"国内观光": ("http://jandan.net/tag/%E5%9B%BD%E5%86%85%E8%A7%82%E5%85%89", None),
        u"史海钩沉": ("http://jandan.net/tag/%E5%8F%B2%E6%B5%B7%E9%92%A9%E6%B2%89", None),
    },
    u"人类": {
        u"美女": ("http://jandan.net/tag/%E7%BE%8E%E5%A5%B3", None),
        u"熊孩子": ("http://jandan.net/tag/%E7%86%8A%E5%AD%A9%E5%AD%90", None),
        u"大丈夫": ("http://jandan.net/tag/%E5%A4%A7%E4%B8%88%E5%A4%AB", None),
        u"笨贼": ("http://jandan.net/tag/%E7%AC%A8%E8%B4%BC", None),
        u"真的猛士": ("http://jandan.net/tag/%E7%9C%9F%E7%9A%84%E7%8C%9B%E5%A3%AB", None),
        u"正能量": ("http://jandan.net/tag/%E6%AD%A3%E8%83%BD%E9%87%8F", None),
    },
    u"折腾": {
        u"减肥": ("http://jandan.net/tag/%E5%87%8F%E8%82%A5", None),
        u"整形": ("http://jandan.net/tag/%E6%95%B4%E5%BD%A2", None),
        u"变性": ("http://jandan.net/tag/%E5%8F%98%E6%80%A7", None),
        u"健康": ("http://jandan.net/tag/%E5%81%A5%E5%BA%B7", None),
        u"教育": ("http://jandan.net/tag/%E6%95%99%E8%82%B2", None),
        u"旅游": ("http://jandan.net/tag/%E6%97%85%E6%B8%B8", None),
    },
    u"NSFW": {
        u"SEX": ("http://jandan.net/tag/sex", None),
        u"WTF": ("http://jandan.net/tag/wtf", None),
        u"同性恋": ("http://jandan.net/tag/%E5%90%8C%E6%80%A7%E6%81%8B", None),
        u"重口味": ("http://jandan.net/tag/%E9%87%8D%E5%8F%A3%E5%91%B3", None),
        u"何其低俗焉": ("http://jandan.net/tag/%E4%BD%95%E5%85%B6%E4%BD%8E%E4%BF%97%E7%84%89", None),
        u"没品笑话集": ("http://jandan.net/tag/%E6%B2%A1%E5%93%81%E7%AC%91%E8%AF%9D%E9%9B%86", None),
    }

}
```

### PanSci 范科学
url: http://pansci.asia/

```python
CATEGORIES = {
    u"内容分类": {
        u"人体解析": ("http://pansci.asia/archives/category/type/humanbeing", None),
        u"地球脉动": ("http://pansci.asia/archives/category/type/earth", None),
        u"自然生态": ("http://pansci.asia/archives/category/type/nature", None),
        u"太空探索": ("http://pansci.asia/archives/category/type/space", None),
        u"万物之理": ("http://pansci.asia/archives/category/type/%E7%89%A9%E7%90%86-%E5%8C%96%E5%AD%B8", None),
        u"医疗疾病": ("http://pansci.asia/archives/category/type/medicine-disease", None),
        u"文明足迹": ("http://pansci.asia/archives/category/type/%E6%96%87%E6%98%8E%E8%B6%B3%E8%B7%A1", None),
        u"环境与我": ("http://pansci.asia/archives/category/type/environment", None),
        u"生命奥秘": ("http://pansci.asia/archives/category/type/lifescience", None),
        u"科学传播": ("http://pansci.asia/archives/category/type/scicomm", None),
        u"科技前言": ("http://pansci.asia/archives/category/type/technology", None),
    }
}
```

### 喷嚏网
url: http://www.dapenti.com/blog/index.asp
废弃：http://www.dapenti.com/blog/blog.asp?subjectid=108&name=agile

### 豆瓣 Tag
url: https://www.douban.com/
待增加: 涨姿势 http://www.douban.com/tag/%E6%B6%A8%E5%A7%BF%E5%8A%BF/?source=topic_search

### FT 中文网
url: http://www.ftchinese.com/
废弃: 更新速度非常慢
- http://www.ftchinese.com/channel/life.html 生活时尚/生活话题
- http://www.ftchinese.com/channel/pursuit.html 乐尚街

### 物质生活
url: http://materielle.cn/index.aspx?Class_id=1
废弃: 最新文章还是 2015 年 11 月的
- http://materielle.cn/fashion.aspx?Class_id=2
- http://materielle.cn/fashion.aspx?Class_id=3
- http://materielle.cn/fashion.aspx?Class_id=4
- http://materielle.cn/fashion.aspx?Class_id=7

### 好莱坞电影手册
url: http://moviesoon.com/news/
待增加: http://moviesoon.com/news/ 影像日报

```python
CATEGORIES = {
    u"影像日报": ("http://moviesoon.com/news/", None)
}
```

### 中国新闻网
url: http://www.chinanews.com/

```python
CATEGORIES = {
    u"国内": ("http://www.chinanews.com/china.shtml", None),
    u"国际": ("http://www.chinanews.com/world.shtml", None),
    u"军事": ("http://www.chinanews.com/mil/news.shtml", None),
    u"社会": ("http://www.chinanews.com/society.shtml", None),
    u"财经": ("http://finance.chinanews.com/cj/gd.shtml", None),
    u"产经/房产": ("http://www.chinanews.com/house/gd.shtml", None),
    u"产经/IT": ("http://it.chinanews.com/it/gd.shtml", None),  # 待添加
    u"产经/能源": ("http://www.chinanews.com/energy/gd.shtml", None),
    u"金融": ("http://fortune.chinanews.com/", None),  # 待解析
    u"汽车": ("http://auto.chinanews.com/", None),  # 待解析
    u"港澳": ("http://www.chinanews.com/compatriot.shtml", None),
    u"台湾": ("http://www.chinanews.com/taiwan.shtml", None),
    u"华人": ("http://www.chinanews.com/huaren.shtml", None),
    u"华报": ("http://www.chinanews.com/hb.shtml", None),
    u"娱乐": ("http://www.chinanews.com/entertainment.shtml", None),
    u"体育": ("http://www.chinanews.com/ty/gun-news.html", None),
    u"文化": ("http://www.chinanews.com/wenhua.shtml", None),
    u"理论": ("http://www.chinanews.com/theory.shtml", None),
    u"生活/健康": ("http://www.chinanews.com/jiankang.shtml", None),  # 带添加
    u"游戏": ("", None),
    u"地方": ("", None),
}
```

### 中国摄影出版社
url: http://www.cpph.com/
废弃: http://www.cpph.com/category/news/share

### 凤凰网
url: http://www.ifeng.com/

```python
CATEGORIES = {
    u"资讯": {
        u"大陆": ("http://news.ifeng.com/mainland/index.shtml", None),
        u"国际": ("http://news.ifeng.com/world/index.shtml", None),
        u"台湾": ("http://news.ifeng.com/taiwan/index.shtml", None),
        u"军事": ("http://news.ifeng.com/mil/index.shtml", None),  # 待解析
        u"社会": ("http://news.ifeng.com/society/index.shtml", None),
        u"图片": ("http://photo.ifeng.com/", None),  # 大图新闻, 待解析
        u"评论": ("http://news.ifeng.com/opinion/", None),  # 待解析
        u"历史": ("http://news.ifeng.com/history/", None),  # 待解析
        u"文化": ("http://culture.ifeng.com/", None),  # 待解析
        u"国学": ("http://guoxue.ifeng.com/", None),  # 待解析
    },
    u"财经": {
        # u"宏观": ("http://finance.ifeng.com/macro/", None), 待解析
    },
    u"娱乐": {
        u"明星": ("http://ent.ifeng.com/listpage/30282/1/list.shtml", None),
        u"电影": ("http://ent.ifeng.com/listpage/44169/1/list.shtml", None),
        u"电视": ("http://ent.ifeng.com/listpage/44168/1/list.shtml", None),
        u"演出": ("http://ent.ifeng.com/listpage/30741/1/list.shtml", None),
    },
    u"体育": {
        u"中国足球": ("http://sports.ifeng.com/listpage/11244/1/list.shtml", None),
        u"国际足球": ("http://sports.ifeng.com/listpage/11246/1/list.shtml", None),
        u"NBA": ("http://sports.ifeng.com/lanqiu/nba/", None),  # 待解析
        u"CBA": ("http://sports.ifeng.com/lanqiu/cba/", None),  # 待解析
        u"综合": ("http://sports.ifeng.com/listpage/11247/1/list.shtml", None),
        u"独家评论": ("http://sports.ifeng.com/listpage/54063/1/list.shtml", None),
    },
    u"时尚": {
        # 待解析
    },
    u"汽车": {
        # 待解析
    },
    u"房产": {
        # 待解析
    },
    u"科技": {
        u"互联网": ("http://tech.ifeng.com/listpage/803/1/list.shtml", None),
        u"产品": ("http://tech.ifeng.com/product/", None),  # 待解析
        u"智能家庭": ("http://tech.ifeng.com/listpage/26334/1/list.shtml", None),
        u"可穿戴&车科技": ("http://tech.ifeng.com/listpage/26335/1/list.shtml", None),
    },
    u"博报": {
        # 待解析
    },
    u"游戏": {
        # 待解析
    },
}
```

### GQ男士网
url: http://www.gq.com.cn/

```python
CATEGORIES = {
    u"好玩": {
        u"GQ雷达": ("http://www.gq.com.cn/fun/radar/", None),
        u"玩意儿": ("http://www.gq.com.cn/fun/cool-stuff/", None),
        u"GQ研究": ("http://www.gq.com.cn/fun/research/", None),
        u"数据": ("http://www.gq.com.cn/fun/data/", None),
        u"绯闻男人": ("http://www.gq.com.cn/fun/gossip/", None),
        u"语录": ("http://www.gq.com.cn/fun/quote/", None),
    },
    u"潮流": {
        u"男装秀场": ("http://shows.gq.com.cn/", None),
        u"搭配指南": ("http://www.gq.com.cn/fashion/dressing-tips/", None),
        u"流行趋势": ("http://www.gq.com.cn/fashion/trends/", None),
        u"必备单品": ("http://www.gq.com.cn/fashion/item/", None),
        u"时尚圈": ("http://www.gq.com.cn/fashion/news/", None),
    },
    u"腕表": {
        u"新品资讯": ("http://www.gq.com.cn/watch/news/", None),
        u"购表指南": ("http://www.gq.com.cn/watch/guide/", None),
        u"腕表词典": ("http://www.gq.com.cn/watch/wiki/", None),
        u"名家名表": ("http://www.gq.com.cn/watch/collection/", None),
    },
    u"汽车": {
        u"玩家": ("http://www.gq.com.cn/auto/player/", None),
        u"装备": ("http://www.gq.com.cn/auto/equipment/", None),
        u"探索": ("http://www.gq.com.cn/auto/discover/", None),
        u"印象": ("http://www.gq.com.cn/auto/image/", None),
    },
    u"数码": {
        # 待解析
    },
    u"生活": {
        u"吃喝享乐": ("http://www.gq.com.cn/living/leisure/", None),
        u"型男保养": ("http://www.gq.com.cn/living/grooming/", None),
        u"运动健身": ("http://www.gq.com.cn/living/fitness/", None),
        u"性情男人": ("http://www.gq.com.cn/living/dating-and-sex/", None),
        u"CNI餐厅": ("http://www.gq.com.cn/living/cnirestaurants/", None),
        u"职场Boost": ("http://www.gq.com.cn/living/condenastcenter/", None),
    },
    u"女人": {
        # 待解析
    },
    u"人物": {
        u"年度人物": ("http://www.gq.com.cn/tag/91167", None),
    },
}
```

### 和讯财经
url: http://www.hexun.com/

```python
CATEGORIES = {
    u"新闻": {
        # http://news.hexun.com/domestic/
        u"国内": ("http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511056&s=30&cp=1", None),
        # http://news.hexun.com/international/
        u"国际": ("http://open.tool.hexun.com/MongodbNewsService/newsListPageByJson.jsp?id=108511065&s=30&cp=1", None)
    }
}
```

### 韩剧资料馆
url: http://www.hjzlg.com/

```python
CATEGORIES = {
    u"韩娱新闻": ("http://www.hjzlg.com/web5/YCMS_News.asp", None),
}
```

### 环球网
url: http://m.huanqiu.com/

```python
CATEGORIES = {
    u"国际": {
        u"独家报道": ("http://m.huanqiu.com/lm.html?id=33", None),
        u"环球要闻": ("http://m.huanqiu.com/lm.html?id=32", None),
        u"海外看中国": ("http://m.huanqiu.com/lm.html?id=35", None),
    },
    u"国内": {
        u"时政要闻": ("http://m.huanqiu.com/lm.html?id=37", None),
        u"社会万象": ("http://m.huanqiu.com/lm.html?id=113", None),
        # u"图说中国": ("http://m.huanqiu.com/lm.html?id=92", None), # 待解析
    },
    u"军事": {
        u"国际军事": ("http://m.huanqiu.com/lm.html?id=41", None),
        u"中国军事": ("http://m.huanqiu.com/lm.html?id=40", None),
        u"军事评论": ("http://m.huanqiu.com/lm.html?id=90", None),
        u"航天航空": ("http://m.huanqiu.com/lm.html?id=91", None),
        # u"图说军事": ("http://m.huanqiu.com/lm.html?id=43", None),　# 待解析
    },
    u"台海": {
        u"两岸时政": ("http://m.huanqiu.com/lm.html?id=44", None),
        u"台湾社会": ("http://m.huanqiu.com/lm.html?id=46", None),
    },
    u"评论": {
        u"环球今日评": ("http://m.huanqiu.com/lm.html?id=138", None),
        u"国际评论": ("http://m.huanqiu.com/lm.html?id=18", None),
    },
    u"财经": {
        u"中国财经": ("http://m.huanqiu.com/lm.html?id=29", None),
        u"国际财讯": ("http://m.huanqiu.com/lm.html?id=48", None),
    },
    u"科技": {
        u"科技资讯": ("http://m.huanqiu.com/lm.html?id=53", None),
        # u"科技产品": ("http://m.huanqiu.com/lm.html?id=54", None), # 待解析
    },
    u"博览": {
        u"环球博览": ("http://m.huanqiu.com/lm.html?id=114", None),
        # u"有真相": ("http://m.huanqiu.com/lm.html?id=111", None),　# 待解析
    },
    u"娱乐": {
        # u"娱乐图片": ("http://m.huanqiu.com/lm.html?id=59", None), # 待解析
    },
    u"体育": {
        u"体坛资讯": ("http://m.huanqiu.com/lm.html?id=87", None),
        # u"体坛酷图": ("http://m.huanqiu.com/lm.html?id=88", None), # 待解析
    },
    u"健康": {
        u"保健养生": ("http://m.huanqiu.com/lm.html?id=66", None),
        u"健康资讯": ("http://m.huanqiu.com/lm.html?id=137", None),
    },
    u"图片": {
        # u"图说世界": ("http://m.huanqiu.com/lm.html?id=62", None), # 待解析
    },
    u"时尚": {
        u"环球时尚": ("http://m.huanqiu.com/lm.html?id=163", None),
        # u"时尚视觉": ("http://m.huanqiu.com/lm.html?id=162", None), # 待解析
    },
}
```

### 爱范儿
url: http://www.ifanr.com/

```python
CATEGORIES = {
    u"汽车": ("http://www.ifanr.com/category/special/intelligentcar", None),
    u"观察": ("http://www.ifanr.com/category/special/news", None),
    u"新创": ("http://www.ifanr.com/category/special/innovation", None),
    u"商业": ("http://www.ifanr.com/category/special/business", None),
    u"MindTalk": ("http://www.ifanr.com/category/special/mindtalk", None),
    u"产品": ("http://www.ifanr.com/category/special/product", None),
    u"AppSolution": ("http://www.ifanr.com/app", None),
    u"游戏": ("http://www.ifanr.com/category/special/game-special", None),
    u"现场": ("http://www.ifanr.com/category/special/live", None),
    u"译文": ("http://www.ifanr.com/category/special/%E8%AF%91%E6%96%87", None),
    u"故事": ("http://www.ifanr.com/category/special/story", None),
    u"清单": ("http://www.ifanr.com/category/special/%E6%B8%85%E5%8D%95", None),
}
```

### 爱虎趣
url: http://www.ihuqu.com/
废弃：http://www.ihuqu.com/animals/
网站无法访问

### 简书
url: http://www.jianshu.com/
废弃：更新频率太慢，如果需要后期再添加

### 节操精选
url: http://jiecao.fm/news/

```python
CATEGORIES = {
    u"首页": ("http://jiecao.fm/news/", None),
}
```

### 金融界
url: http://www.jrj.com.cn

```python
CATEGORIES = {
    u"财经频道": {
        u"国内财经": ("http://finance.jrj.com.cn/list/guoneicj.shtml", None),
        u"国际财经": ("http://finance.jrj.com.cn/list/guojicj.shtml", None),
        u"产业动态": ("http://finance.jrj.com.cn/list/industrynews.shtml", None),
        u"微学院": ("http://finance.jrj.com.cn/list/weixx.shtml", None),
    },
    u"观点": {
        u"名家专栏": ("http://opinion.jrj.com.cn/list/mjzl.shtml", None),
        u"谈股论金": ("http://opinion.jrj.com.cn/list/tglj.shtml", None),
        u"经济时评": ("http://opinion.jrj.com.cn/list/jjsp.shtml", None),
        u"产业观察": ("http://opinion.jrj.com.cn/list/cygc.shtml", None),
    },
}
```

### 酷狗
url: http://yule.kugou.com/alllist/
废弃: http://yule.kugou.com/alllist/ 很少更新

### M新闻
url: http://news.missevan.cn/

```python
CATEGORIES = {
    u"M新闻": {
        u"动画": ("http://news.missevan.com/news/index?ntype=2", None),
        u"音乐": ("http://news.missevan.com/news/index?ntype=3", None),
        u"游戏": ("http://news.missevan.com/news/index?ntype=4", None),
        u"声优": ("http://news.missevan.com/news/index?ntype=5", None),
        u"小说": ("http://news.missevan.com/news/index?ntype=6", None),
        u"漫画": ("http://news.missevan.com/news/index?ntype=7", None),
        u"Cosplay": ("http://news.missevan.com/news/index?ntype=8", None),
        u"杂志": ("http://news.missevan.com/news/index?ntype=9", None),
        u"周边": ("http://news.missevan.com/news/index?ntype=10", None),
        u"展会": ("http://news.missevan.com/news/index?ntype=11", None),
        u"电影": ("http://news.missevan.com/news/index?ntype=12", None),
        u"萌宅": ("http://news.missevan.com/news/index?ntype=13", None),
        u"杂谈": ("http://news.missevan.com/news/index?ntype=14", None),
        u"DVD/BD": ("http://news.missevan.com/news/index?ntype=15", None),
        u"Other": ("http://news.missevan.com/news/index?ntype=16", None),
    },
}
```

### 南方周末
url: http://www.infzm.com/news.shtml
废弃: http://www.infzm.com/news.shtml 更新较慢，后期再加

### 品读
url: http://www.pento.cn/
废弃: 官方通知，2015-12-1 日起停止服务

### 人民网
url: http://www.people.com.cn/

```python
CATEGORIES = {
    u"时政": {
        u"高层动态": ("http://politics.people.com.cn/GB/1024/index.html", None),
        u"中央部委": ("http://politics.people.com.cn/GB/1027/index.html", None),
        u"人事任免": ("http://politics.people.com.cn/GB/41223/index.html", None),
        u"时事解读": ("http://politics.people.com.cn/GB/389979/index.html", None),
    },
    u"社会": {
        u"本网原创": ("http://society.people.com.cn/GB/86800/index.html", None),
        u"民生报道": ("http://society.people.com.cn/GB/41158/index.html", None),
        u"社会万象": ("http://society.people.com.cn/GB/1062/index.html", None),
    },
    u"法制": {
        u"滚动新闻": ("http://legal.people.com.cn/GB/188502/index.html", None),
    },
    u"观点": {
        u"每日最新评论": ("http://opinion.people.com.cn/GB/159301/index.html", None)
    },
    u"媒体": {
        u"最新资讯": ("http://media.people.com.cn/GB/40606/index.html", None),
    },
    u"国际": {
        u"滚动新闻": ("http://world.people.com.cn/GB/157278/index.html", None),
    },
    u"台湾": {
        u"滚动新闻": ("http://tw.people.com.cn/GB/104510/index.html", None),
    },
    u"财经": {
        u"滚动新闻": ("http://finance.people.com.cn/GB/70846/index.html", None),
    },
    u"IT": {
        u"滚动新闻": ("http://it.people.com.cn/GB/243510/index.html", None),
    },
    u"教育": {
        u"滚动新闻": ("http://edu.people.com.cn/GB/1053/index.html", None),
    },
    u"房产": {
        u"人民出品": ("http://house.people.com.cn/GB/164291/index.html", None),
    },
    u"体育": {
        u"滚动新闻": ("http://sports.people.com.cn/GB/22176/index.html", None),
    },
    u"游戏": {
        u"滚动新闻": ("http://game.people.com.cn/GB/218877/index.html", None),
    },
    u"娱乐": {
        u"独家": ("http://ent.people.com.cn/GB/233357/index.html", None),
    },
    # 本地新闻待抓取
}
```

### 品玩
url: http://www.pingwest.com/

```python
CATEGORIES = {
    u"资讯": {
        u"人物": ("http://www.pingwest.com/category/figure/", None),
        u"现象": ("http://www.pingwest.com/category/phenomenon/", None),
        u"真相": ("http://www.pingwest.com/category/truth/", None),
        u"短新闻": ("http://www.pingwest.com/category/news/", None),
        u"腔调": ("http://www.pingwest.com/category/tune/", None),
        u"酷玩": ("http://www.pingwest.com/category/coolplay/", None),
    },
}
```

### 涂鸦王国
url: http://www.poocg.com/
废弃: http://www.poocg.com/works/new

### 前瞻网
url: http://www.qianzhan.com/
目前解析有点儿问题，需要调整

```python
CATEGORIES = {
    u"快讯": ("http://t.qianzhan.com/kuaixun/", None),
    u"风口": ("http://t.qianzhan.com/fengkou/", None),
    u"企业说": ("http://t.qianzhan.com/qiye/", None),
    u"大咖": ("http://t.qianzhan.com/daka/", None),
    u"科技/业界": ("http://t.qianzhan.com/ind/", None),
    u"科技/互联网": ("http://t.qianzhan.com/int/", None),
    u"科技/手机": ("http://t.qianzhan.com/mob/", None),
    u"科技/汽车": ("http://t.qianzhan.com/car/", None),
    u"科技/智能硬件": ("http://t.qianzhan.com/sma/", None),
    u"大杂会": ("http://t.qianzhan.com/dazahui/", None),
}
```

### 设计癖
url: http://www.shejipi.com/

```python
CATEGORIES = {
    u"首页": ("http://www.shejipi.com/", None),
}
```

### 新浪网
url: http://news.sina.com.cn

```python
CATEGORIES = {
    u"国内": {
        u"内地新闻": ("http://roll.news.sina.com.cn/news/gnxw/gdxw1/index.shtml", None),
        u"港澳台新闻": ("http://roll.news.sina.com.cn/news/gnxw/gatxw/index.shtml", None),
        u"综述分析": ("http://roll.news.sina.com.cn/news/gnxw/zs-pl/index.shtml", None),
    },
    u"国际": {
        u"环球视野": ("http://roll.news.sina.com.cn/news/gjxw/gjmtjj/index.shtml", None),
        u"环球趣闻": ("http://roll.news.sina.com.cn/news/gjxw/hqqw/index.shtml", None),
        # u"海外观察": ("http://news.sina.com.cn/gjzg/", None),  待解析
    },
    u"社会": {
        u"情感八卦": ("http://roll.news.sina.com.cn/news/shxw/zqsk/index.shtml", None),
        u"拍案说法": ("http://roll.news.sina.com.cn/news/shxw/fz-shyf/index.shtml", None),
        u"奇闻趣事": ("http://roll.news.sina.com.cn/news/shxw/qwys/index.shtml", None),
        u"五花八门": ("http://roll.news.sina.com.cn/news/shxw/shwx/index.shtml", None),
        # u"社会热图": ("http://slide.news.sina.com.cn/s/", None),　　# 待解析
    },
    u"军事": {
        # u"图片": ("http://slide.mil.news.sina.com.cn/", None),  # 待解析
        u"深度": ("http://mil.news.sina.com.cn/jssd/", None),
        u"大国博弈": ("http://mil.news.sina.com.cn/dgby/", None),
        u"军史": ("http://mil.news.sina.com.cn/jshm/", None),
    },
    u"评论": {
        # 待解析
    },
    u"体育": {
        # 待解析
    },
    u"娱乐": {
        u"明星/内地强档": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/ndqd/index.shtml", None),
        u"明星/欧美巨星": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/omjx/index.shtml", None),
        u"明星/港台风云": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/gtfy/index.shtml", None),
        u"明星/日韩偶像": ("http://roll.ent.sina.com.cn/ent_more/mxqjc/rhox/index.shtml", None),
        u"音乐/新闻": ("http://roll.ent.sina.com.cn/ent_more/yl2/index.shtml", None),
    },
    u"财经": {
        #   待解析
    },
    u"科技": {
        #   待解析
    },
    u"时尚": {
        # u"时装/民星穿搭": ("http://roll.fashion.sina.com.cn/style/celebrity/index.shtml", None),    #　翻页
        # u"时装/潮流趋势": ("http://roll.fashion.sina.com.cn/style/trend/index.shtml", None),    # 翻页
        # u"时装/热门单品": ("http://roll.fashion.sina.com.cn/style/accessories/index.shtml", None),      # 翻页
        u"时装/时尚资讯": ("http://roll.fashion.sina.com.cn/style/info/index.shtml", None),
        # u"时装/产业观察": ("http://roll.fashion.sina.com.cn/style/industry/index.shtml", None),
        # u"时装/时尚人物": ("http://roll.fashion.sina.com.cn/style/icon1/index.shtml", None),
        # u"时装/奢华珠宝": ("http://roll.fashion.sina.com.cn/style/jewelry/index.shtml", None),
        u"时装/购物信息": ("http://roll.fashion.sina.com.cn/style/shopping/index.shtml", None),

        # u"美容/护肤": ("http://roll.fashion.sina.com.cn/beauty/skincare/index.shtml", None),
        # u"美容/彩妆": ("http://roll.fashion.sina.com.cn/beauty/makeup/index.shtml", None),
        # u"美容/美发": ("http://roll.fashion.sina.com.cn/beauty/hair/index.shtml", None),
        u"美容/资讯": ("http://roll.fashion.sina.com.cn/beauty/news/index.shtml", None),

        # u"美体/减肥瘦身": ("http://roll.fashion.sina.com.cn/body/fit/index.shtml", None),
        # u"美体/私密地带": ("http://roll.fashion.sina.com.cn/body/secret/index.shtml", None),
        # u"美体/性爱宝典": ("http://roll.fashion.sina.com.cn/body/sex/index.shtml", None),
        # u"美体/健康热点": ("http://roll.fashion.sina.com.cn/body/health/index.shtml", None),
        # u"美体/身体艺术": ("http://roll.fashion.sina.com.cn/body/tattoo/index.shtml", None),
        # u"美体/身体护理": ("http://roll.fashion.sina.com.cn/body/care/index.shtml", None),

        u"尚品/产业": ("http://roll.fashion.sina.com.cn/luxury/sinfo/index.shtml", None),
        u"尚品/豪车": ("http://roll.fashion.sina.com.cn/luxury/cars/index.shtml", None),
        # u"尚品/数码": ("http://roll.fashion.sina.com.cn/luxury/fun/index.shtml", None),   # 时间
        u"尚品/度假酒店": ("http://roll.fashion.sina.com.cn/luxury/leisure/index.shtml", None),
        u"尚品/豪宅": ("http://roll.fashion.sina.com.cn/luxury/design/index.shtml", None),
        u"尚品/游艇": ("http://roll.fashion.sina.com.cn/luxury/aeromarine/index.shtml", None),

        u"婚嫁/盛装新娘": ("http://roll.fashion.sina.com.cn/wedding/dresses/index.shtml", None),
        u"婚嫁/珠宝钻戒": ("http://roll.fashion.sina.com.cn/wedding/rings/index.shtml", None),
        u"婚嫁/婚礼殿堂": ("http://roll.fashion.sina.com.cn/wedding/ceremony/index.shtml", None),
        u"婚嫁/蜜月旅行": ("http://roll.fashion.sina.com.cn/wedding/honeymoon/index.shtml", None),
        u"婚嫁/婚恋私语": ("http://roll.fashion.sina.com.cn/wedding/relationship/index.shtml", None),
        u"婚嫁/名人婚事": ("http://roll.fashion.sina.com.cn/wedding/star/index.shtml", None),
    }
}
```

# 缓存说明

#### spider name
spider:news:name 如: spider:news:news163

#### news
"news:" + base64.urlsafe_b64encode(string).replace("=", "")

#### wechat openid and channel info
news:wechat:openid 如: news:wechat:oIWsFt_60J20VTUbAEOviZNWlmcQ

# 新闻类网站模式说明

- 列表页为ajax请求，详情页为html(常见)
- 列表页为html请求，详情页为html(常见)
- 列表页为ajax请求，详情页为ajax请求(少见)
- 页面比较混杂，需通过配置跟踪链接

# 新闻内容解析服务说明

- 链接转为绝对地址(urlparse.urljoin)
- 清洗策略
	1. 基础清洗，去掉script, link 等无用内容，清洗后的内容可供标题，时间，作者，摘要抽取
	2. 抽取清洗，为打分确定内容容器标签，移除无用标签，只保留特定的一些标签，清洗后的内容供打分使用
	3. 内容清洗，移除内容中的垃圾信息，如广告，版权声明等(需配置)，清洗后的内容供内容抽取
- 确定支持的标签定位方法: bs4 find_all select

## 标签定位参数格式说明
```python
{"method": "find_all", "params": {"name": None, "attrs"={}, recursive=True, limit=None, "id"="test", "href"="http://www.test.com/", "class_"="content body"}, "nth": 0}
{"method": "select", "params": {"selector": "css string", limit=None}, "nth": 0}
```