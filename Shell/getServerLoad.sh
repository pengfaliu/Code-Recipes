#!/bin/bash
# Author  : bjqinling@360buy.com
# Date    : 2013-1-16
# Version : 2.0
# Usage   : Get Server Load
#

export LANG=C
_load=`sar|tail -n 1|awk '{print $NF}'`
_memAll=`free -m|grep 'Mem:'|awk '{print $2}'`
_memFree=`free -m|grep 'buffers/cache'|awk '{print $NF}'`
_ip=`ifconfig eth0|grep 'inet addr'|awk '{print $2}'|awk -F: '{print $NF}'`
_hostname=`hostname`
_file=`date +%m-%d`-$_ip

#dmidecode  |grep -i -A 1 'Version' |grep -i 'Serial Number:' |awk -F ":" '!($1 in a){a[$1];print $NF}' > /tmp/$_file

_sn=`/usr/sbin/dmidecode  |grep -i -A 1 'Version' |grep -i 'Serial Number:' |awk -F ":" '!($1 in a){a[$1];print $NF}'`
#SN='1'

#### Gen File ####
echo -e "Hostname\t\t\tIP\t\tLoad\tMemAll/MemFree\tSN" > /tmp/$_file
echo -e "${_hostname}\t${_ip}\t${_load}\t${_memAll}/${_memFree}\t${_sn}" >> /tmp/$_file
#echo -e "${_sn}" >> /tmp/$_file
#### Put File var Ftp ####
cd /tmp
ftp -v -n -i 192.168.129.100 << eof
user upload jdyunwei@upload
cd ServerStatus
bin
put $_file
close
bye
eof
#### Remove File ####
#rm -f  /tmp/$_file
