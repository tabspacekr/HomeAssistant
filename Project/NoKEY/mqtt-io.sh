#!/bin/bash
cp /root/config.yml_original /root/config.yml
pkill -9 -f "python3 -m mqtt_io /root/config.yml"
HOSTNAME=`echo NK$(ifconfig eth0|grep ether |awk '{print $2}'|cut -f 1-6 -d':'| tr [:lower:] [:upper:] | sed -e 's/://g')`
sed -i "s/HOSTNAME/$HOSTNAME/g" /root/config.yml
nohup python3 -m mqtt_io /root/config.yml > /dev/null 2>&1 &
