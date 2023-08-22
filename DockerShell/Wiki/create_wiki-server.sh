# mkdir ./tmp
# cd ./tmp
# wget https://releases.wikimedia.org/mediawiki/1.40/mediawiki-1.40.0.tar.gz
# tar -xvzf ./mediawiki-*.tar.gz
# sudo mkdir /var/lib/wiki
# sudo mv ./mediawiki-*/* /var/lib/wiki

echo "创建 wiki-server 挂载目录 "
./prepare_wiki_volume.sh

docker run -d -t -p 2080:80 --name wiki-server -v /data/wiki:/var/www/html/wiki --network stormphoenix-net --privileged=true stormphoenix/wikiserver:v1.0 /root/start_apache2_service.sh
