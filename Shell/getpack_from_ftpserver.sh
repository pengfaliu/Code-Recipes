#!/bin/sh                                                                                                              
# fapeng.liu
# date: 2016.1.21
# get zip or war and show extension name
#
# version 1.0.1
#
 
basedir="/home/finance/App/"
 
if [[ $# -eq 0 ]];then
   echo "Usage `basename $0` url"
else
   URL=$1
   wget --ftp-user=download --ftp-password=donly2015 $URL
   basefilename=$(basename $URL)
   filename=${basefilename%.*}
   extension=${basefilename##*.}
   if [ "x$extension" == "xzip" ];then
      echo "this file is zip compress."
      unzip $basefilename
      echo "delete $basefilename"
      /bin/rm -f $basefilename
   elif [ "x$extension" == "xwar" ];then
      echo "this file is war compress."
      unzip $basefilename
      echo "delete $basefilename"
      /bin/rm -f $basefilename
   else
     echo "unknown file extension or other error."
   fi
fi
