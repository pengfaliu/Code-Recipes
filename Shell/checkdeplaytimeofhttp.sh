#!/bin/bash
# 
# unit of time is second 
if [[ "x$1" == "x" ]];then
    echo "Usage: $0 URL"
else
    echo "\taccess web server time list: [http://$1]"
    curl -o /dev/null -s -w "\thttp_status_code:%{http_code}\n \thttp_connect_time:%{http_connect}\n \
\tDNS_query_time:%{time_namelookup}\n\tTCP_time_connect:%{time_connect}\n\ttime_pretransfer:%{time_pretransfer}\n \
\ttime_starttransfer:%{time_starttransfer}\n\ttime_total:%{time_total} seconds \n\tsize_download:%{size_download} \byte\n\tspeed_download:%{speed_download} kb/s\n\n" $1
fi