#!/usr/bin/env bash


# 一点资讯
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:yidianzixun
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:yidianzixun

# 今日头条
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:toutiao
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:toutiao
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:toutiaohao

# 网易新闻
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news163
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:news163

# 微信评论
# curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:wechat

# 新浪
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:roll_news_sina_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:mil_news_sina_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:tech_news_sina_com_cn_zl
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:fashion_sina_cn

# 搜狐
# curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news_sohu_com
# curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_sohu_com

# 腾讯
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news_qq_com

# zaker
# curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:app_myzaker_com

