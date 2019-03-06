#/usr/bin/python
#-*- coding: UTF-8 -*-
#
#
#
# 解密
# for unix

import base64
import sys



#----------------------------------------------------------------------
def decrypt(strings):
    """decrypt some strings,and print sting"""
    originstr = base64.decodestring(strings)
    output = originstr[0:-18]
    print output
    
  
if __name__ == '__main__':
    decrypt(sys.argv[1])
    
    
    