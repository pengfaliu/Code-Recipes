#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        httpclient
# Author:      pengfaliu
# Email:       pengfaliu@163.com	
# Created:     7/03/2019 d/m/y
# requirement: python >=2.6
# version 1.0
#-------------------------------------------------------------------------------
import httplib
import urllib
import os,sys
import urlparse

#import urllib2

########################################################################
class httpclient:
    """
    不使用库，自己可以利用正则表达式实现解析域名各部分参数：协议、域名、端口、路径、载荷等。

    使用的正则表达式如下：
    
    r'''(?x)\A
    ([a-z][a-z0-9+\-.]*)://　　　　　　　　　　　　　# Scheme
    ([a-z0-9\-._~%]+　　　　　　　　　　　　　　　　　# IPv4 host
    |\[[a-z0-9\-._~%!$&'()*+,;=:]+\])　　　　　　　# IPv6 host
    (:[0-9]+)?　　　　　　　　　　　　　　　　　　　　　# Port number
    ([a-zA-Z0-9\-\/._~%!$&'()*+]+)?　　　　　　　　# path
    (\?[a-zA-Z0-9&=]+)?　　　　　　　　　　　　　　　　# query
    '''              
　　例如，对于"https://www.baidu.com/xxx/xxx?s=xxx"网址，解析出来各部分为：
   ('https', 'www.baidu.com', None, '/xxx/xxx', '?s=xxx')
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.httpClient =  None
        self.defaultport = 80
        self.defaultheader = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    #get调用
    #----------------------------------------------------------------------
    def post(self,url,port=80,header=None,body=None):
        """"""
    
        try:
            params=urllib.urlencode({'account':'1350000','password':'0000','roleType':1,'zoneCode':'北京市'})
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
            self.httpClient=httplib.HTTPConnection("xxx.xxx.com",80,timeout=30)
            self.httpClient.request("POST","/educmbs/member/login.htm",params,headers)
        
            response=self.httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
            print response.getheaders()
        
        except Exception,e:
            print e
        
        finally:
            if self.httpClient:
                self.httpClient.close()
    #----------------------------------------------------------------------
    def get(self,url,port=80):
        """"""
        #解析url
        urlnew= urlparse.urlparse(url)
        hostname = urlnew.hostname
        path = urlnew.path
        try:
            self.httpClient=httplib.HTTPConnection(hostname,port,timeout=30)
            self.httpClient.request("GET",path)
            
            #response 是httpresponse对象
            response= self.httpClient.getresponse()
            print response.status
            print response.reason
            print response.read()
        
        except Exception,e:
            print e
            
        finally:
            if self.httpClient:
                self.httpClient.close()
    
    
if __name__ == "__main__":
    httpclient=httpclient()
    url="https://www.cnblogs.com/tomato0906/articles/4657477.html"
    print httpclient.get(url)