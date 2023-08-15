docker run -d -p 1080:80 --name wordpress-server --network stormphoenix-net -v "/data/wordpress/www/html":/var/www/html/ wordpress
