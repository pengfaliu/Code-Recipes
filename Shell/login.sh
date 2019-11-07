#!/bin/sh
for line in `cat ip.conf`
do 
#scp $@ root@$line:/export/data/tomcatRoot/360_buy_search/server/data/ 
ssh  $line
done 
