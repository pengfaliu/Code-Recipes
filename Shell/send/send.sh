#!/bin/sh
#Author LiuFaPeng
#
#auto bat deploy
#
#Example: scriptsname zip  project_name 
_PATH=/root/upload/
_DIR_PROJECT=/export/data/tomcatRoot/
if [ "$#" != "2" ];then

                echo;echo -e "\033[33m Usage:$(basename $0) zip  project_name \033[0m"
                echo;echo "Example:";echo;
                echo -e "\033[47;30m $(basename $0) zip passport.360buy.com  \033[0m"
                exit 1
fi
##excute 
for _LINE in $(cat ip.conf|grep -v "^#")
do 
	echo -e "\033[33m $_LINE starting.... \033[0m"
	#send packge to other  $1 is zip packge
	scp  ${_PATH}$1  root@${_LINE}:${_PATH}
	#$2 is project name
	ssh   root@$_LINE "cd ${_DIR_PROJECT};echo backup......;${_PATH}back*sh $2  &&  cd ${_DIR_PROJECT}$2 && unzip -o ${_PATH}$1 && echo successful!"
	echo  -e "\033[42;37m $_LINE end \033[0m"
done 
