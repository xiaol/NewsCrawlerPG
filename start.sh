#!/bin/sh


nohup scrapy crawl spider:news:news163 &
echo 'start news163 spider'
nohup scrapy crawl spider:news:toutiao &
echo 'start toutiao spider'
nohup scrapy crawl spider:news:yidianzixun &
echo 'start yidianzixun spider'

