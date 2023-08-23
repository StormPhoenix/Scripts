mkdir -p /data/controller
docker run -d -t --name controller -v /data/controller:/data/controller --network stormphoenix-net --privileged=true stormphoenix/controller:v1.0 /bin/bash
