#!/bin/bash

./build_halo_jar.sh

mkdir ~/myblog
chmod 755 ~/myblog
cp ./halo-1.6.0-SNAPSHOT.jar ~/myblog/

cd ~
unzip ./halo-backup.zip && rm halo-backup.zip


