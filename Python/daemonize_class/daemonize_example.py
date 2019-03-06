#!/usr/bin/python
#coding:utf8
# daemon 

from time import sleep   
import os,sys   
from daemonize import Daemonize   
    
pid = "/tmp/test.pid" 
    
def wlog():   
    f=open('/tmp/nima','a')   
    f.write('11')   
    f.close()   
    
def main():   
    while True:   
        sleep(5)   
        wlog()   
    
daemon = Daemonize(app="test_app", pid=pid, action=main)   
daemon.start()   
daemon.get_pid()   
daemon.is_running() 