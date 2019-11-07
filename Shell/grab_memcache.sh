#!/bin/sh
netstat -antlp|grep memcached |awk '{print $5}'|cut -d: -f1|sort|uniq|grep -v \*  >> `ifconfig eth0|grep "inet addr"|gawk -F : '{print $2}'|gawk  '{print $1}'`.txt  
