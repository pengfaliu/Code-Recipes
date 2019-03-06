#!/usr/bin/python
# -*- coding: utf8 -*-_
#-------------------------------------------------------------------------------
# Name:        Zabbix Monitor Nginx Status
# Author:      baoshun.wang@msfinance.cn
# Created:     2015/07/03
#-------------------------------------------------------------------------------

import urllib2, re, json


def main():
    nginx_status_key = ['Active','Accepted','Handled','Requests','Reading','Writting','Waitting']
    Nginx_url = "http://127.0.0.1/status"
    Nginx_req = urllib2.Request(Nginx_url)
    Nginx_res = urllib2.urlopen(Nginx_req)
    Output_key = re.findall(r'\d{1,8}', Nginx_res.read())

    for i in range(1,3,1):
        Output_key[i] = int(Output_key[i]) - 1

    nginx_status = dict(zip(nginx_status_key,Output_key))

    print json.dumps(nginx_status)
if __name__ == '__main__':
    main()