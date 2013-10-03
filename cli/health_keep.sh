#!/bin/bash

####################
# called from cron #
####################

# read conf
clidir=$(cd $(dirname $0); pwd)
. $clidir/conf

# get server response time
cmd="curl -kL ${SERVER_URL} --max-time 20 --output /dev/null --write-out %{time_total}"
server_response=`${cmd}`

# evaluate
compare="${server_response} > ${LIMIT_TIME}"
exceeded=`echo $compare | bc`

# send mail and restart if it's too solow
if [ $exceeded -gt 0 ];then
    # restart server
    sh $clidir/app.sh restart
    # send mail
    subject="[ocr-kcwidget] RESPONSE TOO SLOW"
    content="${compare}\nRESULT : ${result}\nServer Restarted"
    echo "${content}" | mail -s "${subject}" "${EMAIL}" --
else 
    # OK, pass
    :
    #echo 'Regular health check is OK : '$compare
fi
