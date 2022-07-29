FROM debian:11
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
  apt-get -y upgrade && \
  apt-get -y install bundler && \
  gem install github-pages && \
  gem install webrick
