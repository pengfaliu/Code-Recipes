#!/usr/bin/env python
#
#
#
#
#

import urllib2
import 
def get_mobile_area(phone_num):
    api='http://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel='+phone_num
    urllib2.