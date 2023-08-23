mkdir /data/controller
docker run -d -t --name controller -v /data/controller:/data/controller --network stormphoenix-net --privileged=true ubuntu:latest /bin/bash
