#!/bin/sh
for _LINE in `cat $1|grep -v "^#"`
do 
echo -e "\033[31m  You loginning...$_LINE \033[0m"
ssh  $_LINE  
done 
