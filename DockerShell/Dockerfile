FROM ubuntu:20.04

MAINTAINER StormPhoenix "stormphoenix.hzau@hotmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install -y openjdk-11-jre
RUN apt-get install -y git
RUN apt-get install -y zip
RUN apt-get install -y wget

RUN mkdir -p /root/blog
RUN chmod 755 /root/blog

COPY halo-1.4.17.jar /root/blog
COPY halo-backup.zip /root/
RUN cd /root && unzip halo-backup.zip && rm halo-backup.zip

EXPOSE 22 80 8080 8090

CMD ["/run.sh"]
