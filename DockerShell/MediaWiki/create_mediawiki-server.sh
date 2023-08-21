./prepare_wiki_data.sh
docker run -d -p 2080:80 --name mediawiki-server --network stormphoenix-net --privileged=true -v "/wiki/LocalSettings.php":/var/www/html/LocalSettings.php -v "/wiki/images/":/var/www/html/images mediawiki:latest
