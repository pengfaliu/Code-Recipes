#/usr/bin/python
#-*- coding: UTF-8 -*-
#
#
#
# 加密
# for unix 

import base64
import random
import sys


upperchr = 'ABCDEFGHIJKLMOPQRSTUVWXYZ'
lowcarsechr = 'abcdefghijklmopqrstuvwxyz'
otherchr = '~!@#$%^&*()?><:;'
numchr =  '1234567890'
mselment = 'xxx.com'

#----------------------------------------------------------------------
def encrypt(strings):
    """encrypt some strings,and print sting"""
    rd = ''.join(random.sample(upperchr+lowcarsechr+otherchr+numchr,10))
    output = base64.encodestring(strings+mselment+rd)
    print output
    
  
if __name__ == '__main__':
    encrypt(sys.argv[1])  
    
    
    
