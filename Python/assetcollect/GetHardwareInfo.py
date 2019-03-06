#!/usr/bin/env python 
#coding:utf-8
#
# gather hardware 

import json
import subprocess
from os import path
from sys import exit

########################################################################
class GetHardwareInfo(object):
    """run shell command and get hardware ,return json data, it need to install lshw package.
    this should be use for centos.
    """

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.lshwpath = "/usr/sbin/lshw"
        if path.isfile(self.lshwpath) is False:
            reason = "%s command dosen't exist please intall it" % self.lshwpath
            print reason
            exit(1)
        else:
            pass
    #----------------------------------------------------------------------
    def _get_hd_info(self):
        """get hardware info and return json data"""
        args=['/usr/sbin/lshw','-json']
        hard_info = subprocess.Popen(args, shell=False)
        print hard_info
        return hard_info
    
if __name__ == "__main__":
    
    unit_test = GetHardwareInfo()
    value = unit_test._get_hd_info()
    print value
        
        
    
    