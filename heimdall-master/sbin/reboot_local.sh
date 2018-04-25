#!/bin/bash
python /root/proxyer/config/genconfig.py
pkill udpxd
pkill rinetd
/usr/local/bin/rinetd -c /root/proxyer/config/rinetd.conf
bash /root/proxyer/config/udpx.sh
