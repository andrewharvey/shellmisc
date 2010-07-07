#!/bin/sh

#polling interval in seconds
interval=1

mkdir logs

#every interval we append the location of the cursor to the log file
#we get a new logfile every hour, but you can use a single log file if you wish
while sleep $interval; do ./mousepos.py >> logs/`date +%Y%m%d%H`.log; done
