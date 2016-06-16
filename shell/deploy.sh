#!/usr/bin/env bash

cd ..
pwd
echo 'deploy project News'
scrapyd-deploy local
echo 'deploy finished'