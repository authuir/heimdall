#! /usr/bin/env python
# -*- coding: utf-8 -*-
# encoding='utf-8'

import os,random,json

cfg = open("/root/proxyer/config/config.json", "r")
fp = open("/var/log/rinetd.log", "r")

json_str = ""
while 1:
    line = cfg.readline()
    if not line:
        break
    json_str = json_str + line.strip('\r\n')
config = json.loads(json_str)


rtn = {}

while 1:
    line = fp.readline()
    if not line:
        break

    lines = line.split()

    try:
        port = lines[3]
        port = int(port)
        input_size = lines[6]
        output_size = lines[7]

        if port not in rtn:
            rtn[port] = {}
            rtn[port]['input'] = 0
            rtn[port]['output'] = 0

        rtn[port]['input'] = rtn[port]['input'] + int(input_size)
        rtn[port]['output'] = rtn[port]['output'] + int(output_size)

    except IndexError as e:
        pass
    except ValueError as e:
        pass
    except Exception as e:
        pass


for i in rtn:
    holder = ""
    limit  = "2.0 GB"

    for ele in config:
        if i == ele[u'Port']:
            holder = ele[u'Name']
            limit  = str(ele[u'Limit'])+"GB"
    i_data = rtn[i]['input']/1024.0/1024.0
    o_data = rtn[i]['output']/1024.0/1024.0
    all_data = i_data+o_data
    
    if i_data > 1024:
        i_data = str(round(i_data/1024.0, 2))+" GB"
    else:
        i_data = str(round(i_data, 2))+" MB"

    if o_data > 900:
        o_data = str(round(o_data/1024.0, 2))+" GB"
    else:
        o_data = str(round(o_data, 2))+" MB"

    if all_data > 100:
        all_data = str(round(all_data/1024.0, 2))+" GB"
    else:
        all_data = str(round(all_data, 2))+" MB"



    print("Port:{0}, \tIn:{1}, \tOut:{2}, \tUsage:{3} of {4}, \t{5} ".format( \
          i, i_data, o_data, all_data, limit, holder))

fp.close()
