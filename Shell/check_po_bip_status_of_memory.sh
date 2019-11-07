
#!/bin/sh
NAME=$(head /export/home/tomcat/sh/active.coupon.360buy.com/tomcat*|grep export|cut -d / -f 6)
PID=$(ps -ef|grep $NAME|grep -v grep|awk '{print $2}')
i=0
while :
do
clear
echo -e "\t$(hostname)\ttimes:$(echo $((30*$i)))\t\tpid:$PID\t$NAME"
jstat -gcutil $PID  1000 30
((++i))
done
