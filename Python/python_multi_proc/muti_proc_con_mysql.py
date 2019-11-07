#!/usr/bin/env python
#coding=utf-8
"""
Author: Squall
Last modified: 2011-10-18 16:50
Filename: pool.py
Description: a simple sample for pool class
"""

from multiprocessing import Pool
from time import sleep
import MySQLdb as mdb
import time
import sys

reload(sys) 
sys.setdefaultencoding('utf-8') 
con = None


def f(x):
    for i in range(10):
        print '%s --- %s ' % (i, x)
        #sleep(10)
        try:
            #连接mysql的方法：connect('172.17.19.137','dnstest_w','dnstest_w','dbname')
            con = mdb.connect('testmysql.jddb.stg','dnstest_w',
                'dnstest_w', 'dnstest',3358,charset='utf8');
            #con = mdb.connect(host="172.17.19.137",user="dnstest_w",passwd="dnstest_w",db="mytable",charset="utf8",port=3358)
            #所有的查询，都在连接con的一个模块cursor上面运行的
            cur = con.cursor()
            #执行一个查询
            cur.execute("SELECT VERSION()")
            #取得上个查询的结果，是单个结果
            data = cur.fetchone()
            print "Database version : %s " % data
        finally:
            if con:
                #无论如何，连接记得关闭
                con.close()

def main():
    pool = Pool(processes=30)    # set the processes max number 3
    for i in range(11,20):
        result = pool.apply_async(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print 'successful'


if __name__ == "__main__":
    main()
