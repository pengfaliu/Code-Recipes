#!/bin/bash
############################################################
# version 1.0.0
# Author: pengfaliu@163.com
# Date: 2014-07-16
# 
# description :
#       this scripts will be creat enviroment of rpm build 
#       it generate some directories in you home.
#	note: if you are root,you will be choose somethings.
############################################################

. /etc/profile



Installsoft()
{
	yum -y install rpm-build redhat-rpm-config
}

Createnvdir()
{
	mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
	echo "%_topdir $HOME/rpmbuild" > ~/.rpmmacros
	exit 0

}

Getf()
{
home=$(grep $1 /etc/passwd|awk -F ':'  '{print $6}')
cat << EOF >/tmp/c.sh 
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
echo "%_topdir $home/rpmbuild" > ~/.rpmmacros
exit 0
EOF
chmod +x /tmp/c.sh
}

Changedefaultdir()
{
	if [[ "`whoami`" = "root" ]];then
		read -p "Do you creat rpmbuild env in home directory of root,it's not suggest...(y/n) "  choice
		if [[ "$choice" = "y" ]];then
			Createnvdir
			echo "rpm-build env has been created successfully in root home"	
		elif [[ "$choice" = "n" ]];then
			read -p "please input a common user name: " username
			#su - $username  -c Createnvdir
			if $(id $username >/dev/null 2>&1);then
				Getf $username
				su - $username  -c /tmp/c.sh
				echo "rpm-build env has been created successfully in $username home"	
			else
			   echo "$username do not exist! try again."
			   Changedefaultdir
			fi
		fi
	else 
		Createnvdir
		echo "rpm-build env has been created successfully in `whoami` home"	
		exit 0
	fi
	
rm -f /tmp/c.sh >/dev/null 2>&1
}

main ()
{

	if ! $(rpm -qa|grep rpm-build >/dev/null 2>&1) && $(rpm -qa|grep redhat-rpm-config >/dev/null 2>&1) ;then
		Installsoft
		Changedefaultdir
	else
		Changedefaultdir
	fi
}	
main 

