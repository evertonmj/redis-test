#!/bin/bash

# 1. Create databases
# apk update && apk upgrade 
# apk add --update alpine-sdk
# apk add --no-cache bash git openssh make cmake

# wget http://download.redis.io/redis-stable.tar.gz
# tar xvzf redis-stable.tar.gz
# cd redis-stable

# make redis-cli
# sudo cp src/redis-cli /usr/local/bin/
# source: ./src/redis-cli -u redis://redis-19735.re-cluster1.ps-redislabs.org:19735
#     SET test:tb:1 "test ok"
# destination:    src/redis-cli -u redis://redis-11027.re-cluster1.ps-redislabs.org:11027
#     GET test:tb:1

# databases removed
SOURCE_DB=redis://redis-12720.re-cluster1.ps-redislabs.org:12720
REPLICA_DB=redis://redis-18151.re-cluster1.ps-redislabs.org:18151

echo "Starting input source databases..."

for value in $(seq 1 100);
do
    redis-cli -u $SOURCE_DB RPUSH list:numbers $value
done

echo "Input source databases finished."

echo "Starting output replica databases..."
for index in $(seq 1 100);
do
    redis-cli -u $REPLICA_DB RPOP list:numbers;
done