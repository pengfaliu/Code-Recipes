#!/usr/bin/env python 
# coding:utf-8
# 
# datetime 对象时间转换成unix 1970年时间
#
# wiki
# python time, datetime, string, timestamp相互转换
#  
# string --> datetime object : datetime.datetime.strptime(str,format)
# datetime object --> string : dt_obj.strftime()
# string --> Time tuple(time_object) : time.strptime(str,format)
# Time tuple(time_object) --> string : time.strftime(format,t_tp)
# Time tuple(time_object) --> timestamp : time.mktime(t_tp)
# timestamp --> Time tuple(time_object) : time.localtime(ts) or time.gmtime(ts)
# timestamp --> datetime object : datetime.datetime.fromtimestamp(ts)  or timestamp : datetime.datetime.utcfromtimestamp(ts)
# datetime object --> Time tuple(time_object) : dt_obj.timetuple()
# Time tuple(time_object)  --> datetime object : datetime.datetime(t_tp)
"""
##########################
# Python Time Conversion #
##########################

------------------------
-- 一. 时间的表示类型 --
------------------------

py中可能涉及的time有四种类型
    1. time string
    2. datetime tuple(datetime obj)
    3. time tuple(time obj)
    4. timestamp

1. time string
string是最简单的表示time的方式
如如下代码生成的即为string
    ----------------------------------------------
    >>> time.ctime()
    'Mon Dec 17 21:02:55 2012'
    ----------------------------------------------
或者更简单的生成一个字符串
    ----------------------------------------------
    time_string = '2000-01-02 03:04:05'
    ----------------------------------------------

2. datetime tuple(datetime obj)
datetime tuple是datetime.datetime对象类型
    ----------------------------------------------
    >>> datetime.now()
    datetime.datetime(2012, 12, 17, 21, 3, 44, 139715)
    ----------------------------------------------

3. time tuple(time obj)
time tuple是time.struct_time对象类型
    ----------------------------------------------
    time.struct_time(tm_year=2008, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=0, tm_yday=315, tm_isdst=-1)
    ----------------------------------------------

4. timestamp
时间戳类型:自1970年1月1日(00:00:00 GMT)以来的秒数
    ----------------------------------------------
    >>> time.time()
    1355749338.05917
    ----------------------------------------------
    
    
------------------------
-- 二. 类型之间的转换 --
------------------------
1. string 转换为其它
初始化:
    date_str = "2008-11-10 17:53:59"
1.1 string --> datetime obj
导入:
    import datetime
    datetime.datetime.strptime(string, format)
eg
    ----------------------------------------------
    >>> dt_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    >>> dt_obj
    datetime.datetime(2008, 11, 10, 17, 53, 59)
    ----------------------------------------------

1.2 string --> time obj
导入:
    import time
    time.strptime(string, format)
eg
    ----------------------------------------------
    #time模块有类似datetime中的strptime()函数
    >>> date_str = "2008-11-10 17:53:59"
    >>> t_obj = time.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    >>> t_obj
    time.struct_time(tm_year=2008, tm_mon=11, tm_mday=10, tm_hour=17, tm_min=53, tm_sec=59, tm_wday=0, tm_yday=315, tm_isdst=-1)
    ----------------------------------------------

2. datetime obj转换为其它
datetime obj转换为其它类型,用的都是datetime的函数
初始化:
    dt_obj = datetime.datetime(2008, 11, 10, 17, 53, 59)
2.1 dt obj --> string
    ----------------------------------------------
    date_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")
    ----------------------------------------------
2.2 dt obj --> time obj
    ----------------------------------------------
    time_tuple = dt_obj.timetuple()
    ----------------------------------------------

3. time obj转换为其它
初始化:
    time_tuple = (2008, 11, 12, 13, 51, 18, 2, 317, 0)
3.1 time obj --> string
    ----------------------------------------------
    date_str = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
    ----------------------------------------------
3.2 time obj --> datetime obj
    ----------------------------------------------
    datetime.datetime(*time_tuple[0:6])
    ----------------------------------------------
3.3 time obj --> timestamp
    ----------------------------------------------
    ts = time.mktime(time_tuple)
    ----------------------------------------------

4. timestamp转换为其它
初始化:
    timestamp = 1226527167.595983
--!!--注意以下两种都使用local时区
4.1 timestamp --> dt obj
    ----------------------------------------------
    dt_obj = datetime.fromtimestamp(timestamp)
    ----------------------------------------------
4.2 timestamp --> time obj
    ----------------------------------------------
    time_tuple = time.localtime(timestamp)
    ----------------------------------------------
--!!--以下两种方式和时区相关,比较标准时区时间和本地时区时间
4.3 使用UTC --> dt obj
    ----------------------------------------------
    #本地时区时间
    >>> datetime.datetime.fromtimestamp(tm)
    datetime.datetime(2012, 12, 17, 23, 39, 58, 401881)
    #标准时区时间
    >>> datetime.datetime.utcfromtimestamp(tm)
    datetime.datetime(2012, 12, 17, 15, 39, 58, 401881)
    ----------------------------------------------
4.4 使用UTC --> time obj
    ----------------------------------------------
    #本地时区时间
    >>> time.localtime(tm)
    time.struct_time(tm_year=2012, tm_mon=12, tm_mday=17, tm_hour=23, tm_min=39, tm_sec=58, tm_wday=0, tm_yday=352, tm_isdst=0)
    #标准时区时间
    >>> time.gmtime(tm)
    time.struct_time(tm_year=2012, tm_mon=12, tm_mday=17, tm_hour=15, tm_min=39, tm_sec=58, tm_wday=0, tm_yday=352, tm_isdst=0)
    ----------------------------------------------
"""

import datetime
import calendar
import time 


#----------------------------------------------------------------------
def cur_Tzone_to_unix_time():
    """当前时区的时间转换成1970的秒数，有时区的秒数在里面"""
    
    current_time = datetime.datetime.now()
    unix_seconds = calendar.timegm(current_time.timetuple())    
    
    print unix_seconds
    
#----------------------------------------------------------------------
def cur_utc_to_unix_time():
    """当前时区的UTC时间转换成1970的秒数"""
    current_utc_time = datetime.datetime.utcnow()
    unix_seconds = calendar.timegm(current_utc_time.utctimetuple())    
    
    print unix_seconds    

#----------------------------------------------------------------------
def cur_time_to_unix_time():
    """直接给自从1970年到现在的秒数,秒数等同于utc时间"""
    cur_seconds_from_1970 = int(time.time())
    print cur_seconds_from_1970

#----------------------------------------------------------------------
def spec_date_to_unix_time():
    """给定特定的时间转换成1970以来的秒数"""

#----------------------------------------------------------------------
def unix_time_to_locattime(timestamp):
    """从给定的unix时间转换成当前时间"""
    obj_localtime = datetime.date.fromtimestamp(timestamp)
            
if __name__ == '__main__':
    cur_Tzone_to_unix_time()
    cur_utc_to_unix_time()
    cur_time_to_unix_time()
    