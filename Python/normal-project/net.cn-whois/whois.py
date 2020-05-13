#!/usr/bin/env python 
# coding:utf-8
# author :liufapeng
# date : 2015-12-12
#
# util for www.net.cn whois
#
#万网提供了域名查询接口，接口采用HTTP协议：
#接口URL：http://panda.www.net.cn/cgi-bin/check.cgi
#接口参数：area_domain，接口参数值为标准域名，例：52bong.com
#调用举例：
#http://panda.www.net.cn/cgi-bin/check.cgi?area_domain=msxf.com
#返回：
#<?xml version="1.0" encoding="gb2312"?>
#<property>
#<returncode>200</returncode>
#<key>msxf.com</key>
#<original>211 : Domain exists</original>
#</property>
#返回结果说明：
#200 返回码，200表示返回成功
#msxf.com  表示当前查询的域名
#211 : Domain exists 返回结果的原始信息，主要有以下几种

#original=210 : Domain name is available     表示域名可以注册
#original=211 : Domain exists    表示域名已经注册
#original=212 : Domain name is invalid       表示查询的域名无效
#original=213 : Time out 查询超时


import urllib2
import xml.etree.ElementTree as xmlpaser

#----------------------------------------------------------------------
apiurl = 'http://panda.www.net.cn/cgi-bin/check.cgi?area_domain='
def isRegister(domainname):
    """get whois info from  www.net.cn"""
    
    result = urllib2.urlopen(apiurl+domainname)    
    xmlresult = result.read().decode("gb2312").encode('utf-8').replace('gb2312','utf-8')
    #print xmlresult
    root = xmlpaser.fromstring(xmlresult)
    elements = root.getchildren()
    domain = elements[1].text
    reason = elements[2].text.split(':')[1]
    
    print "%s : %s " % (domain,reason)
    
if __name__ == "__main__":
    import sys
    try:
        domain = sys.argv[1]
    except IndexError:
        print "Usage: %s domain" % sys.argv[0]     
        sys.exit(0)
    isRegister(domain)