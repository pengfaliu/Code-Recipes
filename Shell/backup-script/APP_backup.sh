#!/bin/bash
clear
echo "以下应用可用于备份"
#备份目录
BASE="/home/finance/APP/"
#备份目标目录
BACKUP_BASE="/home/finance/.backup/"
#创建备份列表
function create_list(){
	j=1
	for i in `ls $BASE`
	do
		name=$j"."$i
		array[$j]=$name
		((j=$j+1))
		echo $name
	done
	INFO1="请选择要备份的应用: "
	read -p "$INFO1" key
	APP_NAME=`echo ${array[$key]}|awk -F "." '{print $2}'`
	num=`echo $APP_NAME|wc -c`
	if [ $num -eq 1 ]
	then
		echo "错误输入，请重新输入或按ctrl+c退出！"
		sleep 2
		clear
		main	
	fi
}
#备份逻辑
function backup(){
	INFO2="您是否要备份"$APP_NAME"(Y/N): "
	read -p "$INFO2" confirm
#备份开始
	case $confirm in
	"y"|"Y")
		if [ ! -d $BACKUP_BASE$APP_NAME ];
                then
                        mkdir -p $BACKUP_BASE$APP_NAME
                fi
                TIME_STAMP=`date +%Y%m%d"."%H%M`
                zip -qj $BACKUP_BASE$APP_NAME"/"$TIME_STAMP".zip" $BASE$APP_NAME"/"*
                if [ $? -eq 0 ];
                then
                        echo "备份成功,备份结果如下"
                        ls $BACKUP_BASE$APP_NAME
			exit
                else
                        echo "备份失败，请检查！"
                        exit
                fi
	;;
	"n"|"N")
		echo "请重新选择，或按ctrl+c 终止退出！"
		sleep 2
		clear
                main
	;;
	*)	
		echo "输入错误，请重新输入或者按ctrl+c终止退出!"
		sleep 2
		clear
		main
	;;
	esac
}
function main(){
	create_list
	backup
}
while true
do
	main
done