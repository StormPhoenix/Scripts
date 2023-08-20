docker run -d -p 2080:80 --name mediawiki-server --network stormphoenix-net --privileged=true -v "/mediawiki/":/data mediawiki:latest
