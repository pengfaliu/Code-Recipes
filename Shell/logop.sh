#!/bin/bash
IPAD=`ifconfig  | grep 'inet addr:'| grep -v '127.0.0.1' |cut -d: -f2 | awk '{ print $1}'|head -n 1|awk -F . '{print $4}'`
cd /export/servers/apache2/logs/chat.360buy.com/2012/06
if [ -d /export/$IPAD]
then
     echo "the directory $IPAD already exist"
else 
     mkdir -p /export/$IPAD
fi
for FILE in `ls *access*`
do
RESULTDATE=`ls $FILE|awk -F - '{print $1}'|awk -F "" '{print $5$6$7$8}'`
cat $FILE |awk '{print $1 "," $7}'|grep -i "orgid=" >/export/$IPAD/$IPAD"_"$RESULTDATE.txt
sleep 20
done
