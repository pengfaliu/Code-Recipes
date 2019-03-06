#!/bin/bash
clear
echo "����Ӧ�ÿ����ڱ���"
#����Ŀ¼
BASE="/home/finance/APP/"
#����Ŀ��Ŀ¼
BACKUP_BASE="/home/finance/.backup/"
#���������б�
function create_list(){
	j=1
	for i in `ls $BASE`
	do
		name=$j"."$i
		array[$j]=$name
		((j=$j+1))
		echo $name
	done
	INFO1="��ѡ��Ҫ���ݵ�Ӧ��: "
	read -p "$INFO1" key
	APP_NAME=`echo ${array[$key]}|awk -F "." '{print $2}'`
	num=`echo $APP_NAME|wc -c`
	if [ $num -eq 1 ]
	then
		echo "�������룬�����������ctrl+c�˳���"
		sleep 2
		clear
		main	
	fi
}
#�����߼�
function backup(){
	INFO2="���Ƿ�Ҫ����"$APP_NAME"(Y/N): "
	read -p "$INFO2" confirm
#���ݿ�ʼ
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
                        echo "���ݳɹ�,���ݽ������"
                        ls $BACKUP_BASE$APP_NAME
			exit
                else
                        echo "����ʧ�ܣ����飡"
                        exit
                fi
	;;
	"n"|"N")
		echo "������ѡ�񣬻�ctrl+c ��ֹ�˳���"
		sleep 2
		clear
                main
	;;
	*)	
		echo "�������������������߰�ctrl+c��ֹ�˳�!"
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