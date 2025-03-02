# Redis Replication Test Script

## Overview

This Bash script is designed to test Redis replication by inserting values into a source database and then retrieving them from a replica database.

## Prerequisites

Ensure you have Redis installed and running. You will also need:

- Redis Enterprise account created.

- Source and replica databases configured.

- `redis-cli` installed.
    To install redis-cli at your system you can refe
- Environment variables configured for source and replica databases.

## Configuration

- Follow these steps to create and configure source and replica databases:

1. Create a single-sharded Redis Enterprise database named `source-db` with no password, and a memory limit of 2GB. You can learn how to create Redis Enterprise databases [here] (https://redis.io/docs/latest/operate/rs/databases/create/)

2. Enable "Replica Of" by creating another single-sharded Redis Enterprise database named `replica-db` with no password and a memory limit of 2GB. Use source-db as the source database.

3. After creating, obtain source-db and replica-db endpoints and set the following environment variables before running the script:

```sh
export SOURCE_DATABASE_HOST="your-source-redis-host"
export REPLICA_DATABASE_HOST="your-replica-redis-host"
```

Alternatively, you can create a `.env` file and load it using:

```sh
source .env
```

## How It Works

The script pushes numbers from 1 to 100 into a [Redis list](https://redis.io/docs/latest/develop/data-types/lists/) on the source database.

The script then pops these numbers from the replica database to verify replication. Redis List type is naturally ordered, so we don't need to worry about ordering the elements. 

Redis provides commands `RPUSH`, `LPUSH`, `RPOP` and `LPOP`. I used `RPUSH` command to insert the elements at the tail of the list. To get them at the reversed order, I used `RPOP`command to get the last element and print it. By this way it was not necessary to worry with sorting the elements.


## Running the Script

Execute the script using:

```sh
chmod +x replication_test.sh
./replication_test.sh
```

## Expected Output

- Confirmation that numbers were successfully added to the source database by printing it at the console.
- Confirmation that numbers were retrieved from the replica database buy printing them in reverse order..

## Troubleshooting

If replication does not work, ensure the source and replica databases are correctly configured.

- Check if enviroment variables are set correctly with source-db and replica-db endpoints.
- Verify if replication is enabled and if source-db is correctly set as source at replica-db.
- Check the Redis logs to verify that replication is active.

## License

This project is licensed under the MIT License.
