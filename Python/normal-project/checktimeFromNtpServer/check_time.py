#!/usr/bin/env python
# coding: utf-8
# check time from ntp server for zabbix scripts
# __author__ liufapeng
#
#Date :2015-12-12 01:26 

import sys
import time
import datetime
import ntplib
import pytz


########################################################################
class CheckTime(object):
    """This class give you two methods for check time, the first is low precision,and the another one 
    more higher.
    
    low precision of time T>=1 second.
    
    high precision of time 0.01s < T < 1s 
    
    the default precision for time is high.
    
    flag:
        high precision: 2
        low precision: 8
    
    """

    #----------------------------------------------------------------------
    def __init__(self,ntpserver='ntp.msfinance.lo'):
        """precision unit is second(s)"""
        self.server = ntpserver
        self.precision = {'high':0.1,'low':1} 
        self.tz = pytz.timezone('Asia/Chongqing')
        self.host_conn_failed = 64
        
    #----------------------------------------------------------------------
    def highprecision(self,timezone,ntpserver):
        #TODO add multi ntp servers 
        """check time by high precision, caclular the time from 1970-01-01 00:00"""
        try:
            ntp_check_client = ntplib.NTPClient()
            response = ntp_check_client.request(ntpserver, version=4) 
            ntp_time = response.tx_time
            local_time = time.time()
            
        except Exception,e:
            #print e
            #TODO send a warnning message
            sys.exit(self.host_conn_failed)
    
         
        diff_time = local_time - ntp_time
        return float(diff_time)

    #----------------------------------------------------------------------
    def lowprecision(self,timezone,ntpserver):
        """check time by low precision"""
        #TODO add multi ntp servers 
        try:
            ntp_check_client = ntplib.NTPClient()
            response = ntp_check_client.request(ntpserver, version=4)
            ntp_time = datetime.datetime.fromtimestamp(response.tx_time,timezone).second
            local_time = datetime.datetime.now(timezone).second
            
        except ntplib.NTPException:
            #print e
            #TODO send a warnning message
            sys.exit(self.host_conn_failed)
            
        diff_time =  local_time - ntp_time
        return diff_time
    
    def checktime(self,flag=2):
        """base to flag compare to local time with ntp server.
        flag:
        high precision: 2
        low precision: 8
        """
        
        wrong_time = 1
        right_time = 0
        
        if flag == 8:
            diff_time = self.lowprecision(self.tz,self.server)
            if abs(diff_time) < self.precision['low']:
                print right_time
            if abs(diff_time) >= self.precision['low']:
                print wrong_time           
        elif flag == 2:
            diff_time = self.highprecision(self.tz,self.server)
            if abs(diff_time) < self.precision['high']:
                print right_time
            if abs(diff_time) >= self.precision['high']:
                print wrong_time              
            
if __name__ == "__main__":
    
    ck = CheckTime()
    ck.checktime()
