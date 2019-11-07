 netstat -antlp|grep memcached |awk '{print $5}'|cut -d: -f4|sort|uniq|grep -v \*  |tee `ifconfig eth0|grep "inet addr"|gawk -F : '{print $2}'|gawk  '{print $1}'`.txt 

