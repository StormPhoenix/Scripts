FROM ubuntu:20.04

MAINTAINER StormPhoenix "stormphoenix.hzau@hotmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install -y openjdk-11-jre \
    && apt-get install -y git \
    && apt-get install -y zip \
    && apt-get install -y wget

RUN mkdir -p /root/blog \
    && chmod 755 /root/blog

COPY halo-1.4.17.jar /root/blog
COPY halo-backup.zip /root/
COPY run.sh /root/run.sh
RUN chmod +x /root/run.sh

RUN cd /root && unzip halo-backup.zip && rm halo-backup.zip

EXPOSE 22 80 8080 8090

CMD ["/root/run.sh"]
