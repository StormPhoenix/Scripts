docker run -d --name database-server -e MYSQL_ALLOW_EMPTY_PASSWORD=yes --network stormphoenix-net -v /data/mysql-server:/root/Workspace stormphoenix/mysql:latest
cp ./dump_database.sh /data/mysql-server/
cp ./restore_database.sh /data/mysql-server/
