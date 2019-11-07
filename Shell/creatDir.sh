#!/bin/bash
# Author : liufapeng@360buy.com
# Date   : 2012.08.13
# Usage  : Creat Dir

#cd /export/data/ftp
cd .
mkdir  -p $(date +%Y%m%d)
chmod  -R 777 $(date +%Y%m%d)

