#!/usr/bin/env python
#coding:utf-8
#
# copyright 
# license : GPL
# author : liufapeng
#
#  本程在于检测出一个http请求过程中，每个过程所花的时间
# so this program will be use to check time of http delay.
#

import Pycurl

########################################################################
class CheckDelayTimeOfHttp(object):
    """
    http delay time consist of dns query time ,tcp connection time, 
    http request time, server data deal time, http response time, 
    tcp connection close time.
    
    so every fuction return a time.
    
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        
        
    
    

    