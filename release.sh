#!/usr/bin/env bash

echo 'kill all spider process'
ps -ewf | grep spider:news | grep -v grep | awk '{print $2}' | xargs kill -9

echo 'remove pyc'
find -name *.pyc | xargs rm -f

echo 'update project from git'
git pull

echo 'clean logs and eggs in scrapyd'
rm -rf /etc/scrapyd/logs/News/*
rm -rf /etc/scrapyd/eggs/News/*

echo 'deploy project News'
scrapyd-deploy local

echo 'start spiders'
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:news163
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:toutiao
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:yidianzixun
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:comment:wechat
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:i_cri_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:jandan_net
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:jiecao_fm
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:m_huanqiu_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:moviesoon_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news163
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:pansci_asia
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:sina_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:toutiao
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:wechat
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_adaymag_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_chinanews_com
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_gq_com_cn
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_hexun_com
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_hjzlg_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_ifanr_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_ifeng_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_jrj_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_missevan_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_people_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_pingwest_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_qianzhan_com
#curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_shejipi_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:yidianzixun

curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_zaobao_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_oushinet_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_ettoday_net
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:cn_nikkei_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_ltaaa_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_wumaow_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_ftchinese_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_hanjucc_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_hanjumi_net
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_jiemian_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_thepaper_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_chinatimes_com

# add sources v2
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_stnn_cc
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_cankaoxiaoxi_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:roll_news_sina_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:mil_news_sina_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:tech_news_sina_com_cn_zl
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:fashion_sina_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_yicai_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_bjd_com_cn
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_mtime_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news_sohu_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_sohu_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news_17173_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_meizitu_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_7y7_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:news_qq_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:app_myzaker_com
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:toutiaohao
curl http://localhost:6888/schedule.json -d project=News -d spider=spider:news:www_4908_cn