FROM ubuntu:20.04

MAINTAINER StormPhoenix "stormphoenix.hzau@hotmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y vim \
    && apt-get install -y git \
    && apt-get install -y zip \
    && apt-get install -y wget \
    && apt-get install -y apache2 mysql-server \
    && apt-get install -y php php-apcu php-common php-intl php-json php-mysql \
    && apt-get install -y libapache2-mod-php php-xml php-mbstring \
    && apt-get install -y systemctl

COPY start_apache2_service.sh /root/start_apache2_service.sh
RUN chmod +x /root/start_apache2_service.sh

EXPOSE 22 80 2080 8080 8090

CMD ["/root/start_apache2_service.sh"]
