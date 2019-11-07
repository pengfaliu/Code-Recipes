#!/bin/sh
#Author: LiuFaPeng
#Date:2012-08-24 
#
#restart tomcat via  this scripts
#
#$1 ip.conf
#s2 project name
#
#
#
ARGUMENT ()
{
	if [ "$#" = "2" ]
	then
		excute restart order
		for _LINE in $(cat $1|grep -v "^#")
		do 
			echo -e "\033[43;37m  starting ....   $_LINE \33[0m"
				sleep 1
				ssh  $_LINE  "/export/home/tomcat/sh/$2/tomcat"
			echo -e  "\033[42;37m $_LINE has been retarted successfully! \033[0m" 
		done 
		#echo $1  $2
		#echo "$#"
		#echo "hello"
	else
	
		echo;echo -e "\033[33m Usage:$(basename $0) configure_file  project_name \033[0m"
		echo;echo "Example:";echo;
		echo -e "\033[47;30m $(basename $0) ip.conf passport.360buy.com  \033[0m"
		exit 1
	fi
			
}

ARGUMENT  $*
