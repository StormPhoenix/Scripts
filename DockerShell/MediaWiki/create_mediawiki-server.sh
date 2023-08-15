docker run -d -p 2080:80 --name mediawiki-server --network stormphoenix-net --privileged=true -v "/mediawiki/":/var/www/html mediawiki:latest
