#!/usr/bin/env bash

cd ..
pwd

echo 'kill all spider process'
ps -ewf | grep spider:news | grep -v grep | awk '{print $2}' | xargs kill
echo 'kill finished'

echo 'update project from git'
git pull
echo 'pull finished'

echo 'remove pyc'
find -name *.pyc | xargs rm -f
echo 'clean logs and eggs in scrapyd'
rm -rf /etc/scrapyd/logs/News/*
rm -rf /etc/scrapyd/eggs/News/*
echo 'clean finished'

echo 'deploy project News'
scrapyd-deploy local
echo 'deploy finished'

