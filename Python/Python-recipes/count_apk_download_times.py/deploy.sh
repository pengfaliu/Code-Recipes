#!/bin/bash
# 
# install to /home/finance/App/
# deploy count_app.py

log_dir="/home/finance/Logs/count_apk/"
tempfile='/tmp/app_count.tmp'
cronfile="/etc/cron.d/count_apk"
logratefile="/etc/logrotate.d/count_apk"
install_path="/home/finance/App/count_apk/"

if [[ $1 == "deploy" ]]:then

    [ -f $log_dir ] || mkdir $log_dir && chown -R finance.finance $log_dir
    [ -f $install_path ] || mkdir $install_path
    [ -f $tempfile ] || rm -f $tempfile 
    echo "/home/finance/Logs/count_apk/app_download_count.log {
    missingok
    notifempty
    rotate 365
}" > $logratefile


    echo "*/1 * * * * finance /opt/nginx/sbin/count_apk.py" > $cronfile
    chmod +x $install_path/count_apk.py

elif [[ $1 == "uninstall" ]]:then
    rm -f $logratefile $cronfile
    rm -rf $log_dir $tempfile $install_path
fi