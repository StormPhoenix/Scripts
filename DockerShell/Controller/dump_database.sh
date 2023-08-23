#!/bin/bash
now=$(date +'%Y-%m-%d_%H-%M-%S')
filename="Dump_$now.sql"
mysqldump -u root -h database-server --all-databases > "/data/controller/mysql/$filename"
