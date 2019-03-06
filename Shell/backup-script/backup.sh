#!/bin/bash
##! @TODO: Backup APP
##! @AUTHOR: pengfaliu@163.com
##! @VERSION 1.0
##! @DATE: 2015-06-27
##! @Modified Date: 2015-06-27
##! @Review By:


#Define Variables
DIR=$1
DATE=`date +%Y-%m-%d-%H-%M-%S`
BACK_FILE_NAME=$1-$DATE.tar.gz
SOURCE_DIR=$1
DEST_DIR=/home/finance/.backup/$1

#Show the help information
if [ $1 = "-h" ];
then
	echo -e "\e[1;34mPlease useage:  backup.sh DIR \e[0m"
	exit 0
fi
#Check source folder exists
if [ ! -d "$1" ];
then
	echo -e "\e[1;31m######$1 not exit! Please check it and try run this command again!######\e[0m"
	exit 0
fi


#Check the destaton folder exists 
if [ ! -d "$DEST_DIR" ];
then
	echo -e "\e[1;31m######$DEST_DIR not exit!######\e[0m"
	echo -e "\e[1;31m######Now will create Directory $DEST_DIR######\e[0m"
	mkdir $DEST_DIR
	if [ $? -eq 0 ];
	then
		echo -e "\e[1;32m######Create Directory $DEST_DIR Sucefully!######\e[0m"
	else
		echo -e "\e[1;31m######Create Directory $DEST_DIR Failed!######\e[0m"
	fi
fi

#Start run tar command to backup the source folder and save to destation folder
tar -czvf $DEST_DIR/$BACK_FILE_NAME $1 > $DEST_DIR/$DIR-bakckup-$DATE.log 2>&1 
if [ $? -eq 0 ];
then
	echo -e "\e[1;32m######Backup $DIR folder Sucefully!######\e[0m"
else
	echo -e "\e[1;31m######Backup $DIR folder  failed!######\e[0m"
fi

