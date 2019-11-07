#!/bin/sh
#
#Author:LiuFaPeng
#
#version:v-sc-0.0.1
#
#Date:2012-09-04
#
#
SIMPLE_HELP()
{
echo -e "\n\tYou should be choose one,for example:
	`basename $0` [-ssh|-send|-restart|-login|-help] parameters ...
	more detail from  -help"
}

HELP()
{
_SCP_NAME=`basename $0`
echo -e "$_SCP_NAME(1)\t\t\tUser Commands\t\t\t$_SCP_NAME(1)\n\nNAME\n\t$_SCP_NAME - auto deploy progect script\n\nSYNOPSIS\n\t$_SCP_NAME [OPTION]... [PARAMETERS]...\n\nDESCRIPTION\n\tuse this scripts can deploy project automatically that can be creat ssh without key,etc.\n\n\tMandatory arguments to long options are mandatory for short options too.\n\n\t-s,-ssh\n\t\tset up ssh without key.\n\t\t$_SCP_NAME -s password\n\t-S,send\n\t\tautomatic deploy project from ip.conf that include ip address.\n\t\t$_SCP_NAME -S zip project_name\n\t-r,-restart\n\t\t restart project via remote machine.\n\t\t$_SCP_NAME -r ip.conf project_name.\n\t-l,-login \n\t\tnon password login,\n\t\tlogin by ssh without password only one per time\n\t\t$_SCP_NAME -l ip.conf\n\t-o,-order \n\t\t batch execute command include ip.conf\n\t\t$_SCP_NAME -o "commands"\n\t-h,-help\n\t\tdisplay this help\n"
}

EXIST_EXPECT()
{
	_PA_NAME=$(rpm -qa expect|sed -n 1p)
		if [ "-$_PA_NAME" = "-" ];then
			echo -e "\033[34m expect can not found.will install  automatically now,sure?\033[0m"
			read _YN
			case $_YN in
				Y|y)
				yum -y install expect
				;;
				N|n)
				echo "$_SCP_NAME cann't continue,please install expect manually"
				exit
				;;
			esac
		fi

}

EXPECT()
{
	if [ "-$1" = "-" ];then
		echo -e "\033[33mplease input password,you can input multi times if some machines has been set up ssh without key.\n\033[0m"		  
		exit
	else	
			for _IP in `cat ip.conf|grep -v "^#"`
			do 
				expect enable-auto-ssh root@$_IP 22 $1
			done
	fi
}

case $1 in 
	-ssh|-s)
	EXIST_EXPECT
	EXPECT $2
	;;
	-send|-S)
	$PWD/send $2 $3
	;;
	-restart|-r)
	$PWD/remote_restart $2 $3
	;;
	-login|-l)
	$PWD/login $2
	;;
	-order|-o)
	$PWD/order ${2}${3}${4}${5}
	;;
	-help|-h)
	HELP
	;;
	*)
	SIMPLE_HELP
	;;
esac
