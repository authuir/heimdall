#!/bin/bash
kill `ps aux | grep heimdall | grep -v "grep" | awk '{print $2}'`
nohup /root/proxyer/sbin/loki/heimdall.py >> /var/log/heimdall.log 2>&1 &
