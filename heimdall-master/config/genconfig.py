#! /usr/bin/env python
# -*- coding: utf-8 -*-
# encoding='utf-8'

import os,random,json

cfg      = open("/root/proxyer/config/config.json", "r")
f_rinetd = open("/root/proxyer/config/rinetd.conf", "w")
f_udpx   = open("/root/proxyer/config/udpx.sh", "w")
f_ip     = open("/root/proxyer/config/gate.ip", "r")
json_str = ""
remoteip = f_ip.readline()
blockport= []

while 1:
    line = cfg.readline()
    if not line:
        break
    json_str = json_str + line.strip('\r\n')

config = json.loads(json_str)

for ele in config:
    if str(ele[u'Port']) not in blockport:
        f_rinetd.write("0.0.0.0 {0} {1} {2}\n".format(ele[u'Port'], remoteip, ele[u'Remote']))
        f_udpx.write("/usr/local/bin/udpxd -l 0.0.0.0:{0} -t {1}:{2} -v -d\n".format(ele[u'Port'], remoteip, ele[u'Remote']))
f_rinetd.write("logfile /var/log/rinetd.log\n")
f_rinetd.close()
f_udpx.close()
f_ip.close()
cfg.close()