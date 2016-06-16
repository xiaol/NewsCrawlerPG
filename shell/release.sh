#!/usr/bin/env bash

cd ..
pwd

echo 'kill all spider process'
ps -ewf | grep spider:news | grep -v grep | awk '{print $2}' | xargs kill -9
echo 'kill finished\n'

echo 'update project from git'
git pull
echo 'pull finished\n'

echo 'remove pyc'
find -name *.pyc | xargs rm -f
echo 'clean logs and eggs in scrapyd'
rm -rf /etc/scrapyd/logs/News/*
rm -rf /etc/scrapyd/eggs/News/*
echo 'clean finished\n'

echo 'deploy project News'
scrapyd-deploy local
echo 'deploy finished\n'

