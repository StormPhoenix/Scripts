FROM ubuntu:20.04

MAINTAINER StormPhoenix "stormphoenix.hzau@hotmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install -y git \
    && apt-get install -y zip \
    && apt-get install -y wget \
    && apt-get install -y systemctl \
    && apt-get install -y cron mysql-client

RUN mkdir -p /root/Workspace/
COPY Shells/dump_database.sh /root/Workspace/dump_database.sh
COPY Shells/automatically_service.sh /root/Workspace/automatically_service.sh

CMD ["/root/Workspace/automatically_service.sh"]
