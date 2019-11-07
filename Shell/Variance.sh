#!/bin/sh
#Array :the first charcaters is capital only . 
#VARIABLE:all  letters are  capital and first character is underline.
#FUNCTION:all letters are capital only.
# by liufapeng at 2012-07-26 10:59
#variance 
Data=($( awk -F : '{print $2}' net.log |awk  '{print $1}'))
#Data=($( awk -F : '{print $3}' net.log |awk  '{print $1}'))
#Data=($(cat net.log))
_COUNT=${#Data[@]}
AVERAGE(){
	for ((i=0;i<$_COUNT;i++))
	do
	((_SUM=$_SUM+${Data[$i]}))
	done
	#_AVG=$(($_SUM/$_COUNT))    #be suit for ineger but not float
	_AVG=$(echo |awk  '{printf("%0.5f\n",'$_SUM'/'$_COUNT')}')
	echo $_SUM
	echo  "The average  number for IN Bytes is $_AVG"
}
VARIANCE(){
	AVERAGE
	
	for ((i=0;i<$_COUNT;i++))
	do
	_TMP=$(echo |awk  '{printf("%0.5f\n", '${Data[$i]}'-'$_AVG')}')
	_SQUARE=$(echo |awk  '{printf("%0.5f\n", '$_TMP'^2)}')
	_VAR_SUM=$(echo |awk  '{printf("%0.5f\n", '$_VAR_SUM'+'$_SQUARE')}')
	#((_VAR=((_VAR_SUM=$_VAR_SUM+((${Data[$i]}-$_AVG))**2))/$_COUNT))
	done
	_VAR=$(echo |awk  '{printf("%0.5f\n", '$_VAR_SUM'/'$_COUNT')}')
	echo  "The variance number  is $_VAR"
}
	VARIANCE
	

