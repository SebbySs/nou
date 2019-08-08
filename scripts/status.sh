#!/bin/bash

cp /tmp/rpm/index.html /var/www/html

curl -s http://192.168.33.17/index.html | grep "small">> /dev/null 

if [ $? -eq 0 ] ; then
    echo "Success"
else
    echo "Fail"
fi
