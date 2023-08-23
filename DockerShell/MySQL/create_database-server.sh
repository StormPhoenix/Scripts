mkdir -p /data/mysql-server
docker run -d --name database-server -e MYSQL_ALLOW_EMPTY_PASSWORD=yes --network stormphoenix-net -v /data/mysql-server:/root/Workspace stormphoenix/mysql:latest
