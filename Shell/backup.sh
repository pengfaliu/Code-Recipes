#!/bin/bash
# by gupeng 20120425

if [ "$#" = "0" ];then
        echo "#################################################"
        echo "## Usage:$0 arg1 arg2 ...... ##" 
        echo "#################################################"
        exit 1
fi

date=$(date +%Y%m%d%H%M)
dst_dir=/export/data/tomcatRoot
bak_dir=bak
dir_size=512000

cd ${dst_dir}

[ -d "${bak_dir}" ] || mkdir "${bak_dir}"
echo -e -n "\033[0;32;40m"
for ((i=1;i<="$#";i++))
do 
  result=$(eval echo \$$i|tr -d '/')
  #echo $result
  [ -d "$result" ] || { echo "\"$result\" is not exist!";continue; }
  
  [ $(du -s "$result" |awk '{print $1}') -ge "${dir_size}" ] && { echo "\"$result\" is too big.";continue; }

  tar -zcf "${bak_dir}"/"$result".$date.tar.gz "$result"
  if [ "$?" = "0" ];then
     echo  -e -n "\"$result\" --> \"$result.$date.tar.gz\" is ok.\n"
  fi
done  
echo -e "\033[0m"
