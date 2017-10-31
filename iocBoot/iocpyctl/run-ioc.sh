#!/bin/bash

ioc=iocpyctl
port=20000

echo "Checking for updates to apps..."
git pull origin master
if [ $? != 0 ]
then
    make
fi

echo "Starting $ioc on port $port..."
procServ -P $port -L /logs/$ioc.log --logstamp ./st.cmd
