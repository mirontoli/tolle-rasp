#!/bin/bash
# ~/bin/network-monitor.sh
#adapted from https://samhobbs.co.uk/2013/11/fix-for-ethernet-connection-drop-on-raspberry-pi

LOGFILE=/home/mirontoli/network-monitor.log

if /sbin/ifconfig eth0 | grep -q "inet addr:" ;
then
        echo "$(date "+%F %T") : Ethernet OK" >> $LOGFILE
else
        echo "$(date "+%F %T") : Ethernet connection down! Attempting reconnection." >> $LOGFILE
        #/sbin/ifup --force eth0
        /sbin/ifconfig eth0 up              
        if /sbin/ifconfig eth0 | grep -q "inet addr:"; 
        then
            STATE=$(/sbin/ifconfig eth0 | grep "inet addr:")
            echo "$(date "+%F %T") : Network connection reset. Current state is" $STATE >> $LOGFILE
        else
            echo "$(date "+%F %T"): Attempted to reset the network but still not up. Rebooting... Current State is " $STATE >> $LOGFILE
            shutdown -r now
        fi
fi