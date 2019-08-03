#!/bin/bash
PKGS=(
    build-essential
    curl
    libbz2-dev
    libreadline-dev
    libsqlite3-dev
    libssl-dev
    llvm
    make
    wget
    zlib1g-dev
    libmysqlclient-dev
    mysql-server
    pkg-config
    graphviz
    graphviz-dev
    libgraphviz-dev
    unzip
    libfreetype6
    libfreetype6-dev
    supervisor
    memcached
    libmemcached-dev
    libmemcached-tools
    nginx-full
    bsdtar
    inotify-tools
    libmaxminddb0       # GEO
)
sudo apt-get update && sudo apt-get install -y  "${PKGS[@]}"

# NOTE:
#   MySQL ROOT : taberutabi (for Vagrantbox)
