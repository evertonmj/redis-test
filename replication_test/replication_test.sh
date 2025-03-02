#!/bin/bash

SOURCE_DB="redis://$SOURCE_DATABASE_HOST"
REPLICA_DB="redis://$REPLICA_DATABASE_HOST"

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