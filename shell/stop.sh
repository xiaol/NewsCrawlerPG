#!/usr/bin/env bash

echo 'kill all spider process'
ps -ewf | grep spider:news | grep -v grep | awk '{print $2}' | xargs kill 
echo 'kill finished'