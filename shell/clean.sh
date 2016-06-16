#!/usr/bin/env bash

echo 'remove pyc'
find -name *.pyc | xargs rm -f
echo 'clean logs and eggs in scrapyd'
rm -rf /etc/scrapyd/logs/News/*
rm -rf /etc/scrapyd/eggs/News/*
echo 'clean finished'