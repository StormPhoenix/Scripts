FROM ubuntu:20.04

MAINTAINER StormPhoenix "stormphoenix.hzau@hotmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install -y openjdk-11-jre \
    && apt-get install -y git \
    && apt-get install -y zip \
    && apt-get install -y wget \
    && apt-get install -y apache2 mysql-server php php-mysql libapache2-mod-php php-xml php-mbstring \
    && apt-get install -y systemctl \
    && apt-get install -y php-intl

COPY start_apache2_service.sh /root/start_apache2_service.sh
RUN chmod +x /root/start_apache2_service.sh

EXPOSE 22 80 2080 8080 8090

CMD ["/root/start_apache2_service.sh"]
