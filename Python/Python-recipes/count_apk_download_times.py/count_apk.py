#!/usr/bin/env python 
#coding:utf-8
#
#
#"""
#Author:   --<liufapeng>
#Purpose: count amount of android app by nginx log
#Created: 12/15/15
#"""
# 使用crontab的程序统计 android 下载次数，并且发送到大屏幕统计系统

import time
import re
import urllib
import urllib2
import traceback
import sys
import hashlib
import os

import socket 
import struct 
import fcntl 

#----------------------------------------------------------------------
def getlocalipaddr(ifname):
    """return localip strings """
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localipaddr = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0X8915, struct.pack('256s', ifname[:15]))[20:24])  
    return localipaddr

#----------------------------------------------------------------------
def app_count_tempwrite(seeklable):
    """write log byte to temp_file"""
    tempfile = r'/tmp/app_count.tmp'
    f = open(tempfile,'w')
    f.write(seeklable)
    f.close
    return 0
#----------------------------------------------------------------------
def logger(log_name,log_dir,httpresponse=None):
    """write string to file"""
    tm_tag=time.strftime('%Y-%m-%d-%H:%M:%S ')
    if os.path.exists(log_dir):  
        log_fd=open(log_dir+log_name,'a')
        #如果http有响应，记录响应值
        if httpresponse is not None:
            log_fd.write(str(tm_tag)+httpresponse+'\n')
        else:
            log_fd.write(("-"*40)+tm_tag+("-"*40)+"\n")
            traceback.print_exc(file=log_fd)
        log_fd.flush() 
        log_fd.close()
    else:
        print "%s is not exist,please make it." % log_dir
        sys.exit(status=1)    
#----------------------------------------------------------------------
def app_count_tempread():
    """return seeklable"""
    default_seek=0
    tempfile = r'/tmp/app_count.tmp'

    #time 切换00：01 删除写入0
    T = time.strftime('%H%M',time.localtime())
    
    if os.path.exists(tempfile):
        # 程序00点后切换日志了
        if T == '0001':
            app_count_tempwrite(str(default_seek))
            return default_seek 
        else:
            f = open(tempfile,'r')
            seeklable = f.read()
            f.close
            return int(seeklable)
    else:
        # 程序第一次运行
        app_count_tempwrite(str(default_seek))
        return default_seek
     
    
#----------------------------------------------------------------------
def app_count():
    """return app count """
    
    nginx_log = r'/home/finance/Logs/nginx/www.msxf.com/www.msxf.com_access.log' # 可能是动态的
    app_tag = r'.apk'
    
    #如果需要
    BUFSIZE = 10240
    lines = 1000 #每次只处理 1000行
    label = app_count_tempread()
    app_count = 0 #app下载量
    
    fd = open (nginx_log,'r')
    fd.seek(label,0)
    
    for line in fd:
        if re.search(app_tag,line,re.IGNORECASE) is not None:
            app_count = app_count+1
    
    label=app_count_tempwrite(str(fd.tell())) #写临时文件
    fd.close()
    return app_count

#----------------------------------------------------------------------
def post(url,data):
    """return http status code"""
    
    #disable cookie
    req = urllib2.Request(url)
    data1 = urllib.urlencode(data)
    response = urllib2.urlopen(url,data1)
    
    #enable cookie
    #req = urllib2.Request(url) 
    #data = urllib.urlencode(data) 
    #opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
    #response = opener.open(req, data) 
    
    return response.read() 
    
    
#----------------------------------------------------------------------
def main():
    """recode log"""
    log_dir=r"/home/finance/Logs/count_apk/"
    log_name=r"app_download_count.log"
    posturl = r"http://screenback.msxf.lo/screenshow/setdownloadsnum"
    
    
    #安全验证
    tm_tag = time.strftime('%Y-%m-%d-%H:%M:%S')
    tm = tm_tag+'msxf.com'
    sign=hashlib.md5(tm).hexdigest()
    download_count = app_count()
    ipaddr=getlocalipaddr('bond1')
    
    data = {"time":tm_tag,"serverid":ipaddr,"app_count":download_count,"sign":sign,"tm":tm}
    logger(log_name, log_dir, httpresponse=str(data))
    
    #如果下载量为0 则不发送post请求
    if data['app_count'] == 0:
        logger(log_name, log_dir, httpresponse=str(data))
        sys.exit(0)
    else:    
        try:
            code = post(posturl,data)
            logger(log_name, log_dir, httpresponse=str(code))
        except KeyboardInterrupt:
            print "ctrl+c exit."
        except:
            logger(log_name, log_dir)
            logger(log_name, log_dir, httpresponse="error") 
            #traceback.print_exc()


if __name__ == "__main__":
    main()