FROM python:3.10-slim as main

RUN apt-get update && \
   apt-get -y upgrade && \
   apt-get install -y locales locales-all && \
   apt-get -y autoremove && \
   apt-get -y clean

RUN update-locale pt_BR.utf8
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8

RUN pip install Scrapy
RUN pip install json-lines

WORKDIR /opt/sdou

COPY start-container.sh /usr/local/bin/start-container
RUN chmod +x /usr/local/bin/start-container

COPY . /opt/sdou

CMD  [ "bash" ]