Redis Replication Test Script

Overview

This Bash script is designed to test Redis replication by inserting values into a source database and then retrieving them from a replica database.

Prerequisites

Ensure you have Redis installed and running. You will also need:

redis-cli installed.

Environment variables configured for source and replica databases.

Configuration

Set the following environment variables before running the script:

export SOURCE_DATABASE_HOST="your-source-redis-host"
export REPLICA_DATABASE_HOST="your-replica-redis-host"

Alternatively, you can create a .env file and load it using:

source .env

How It Works

The script pushes numbers from 1 to 100 into a Redis list (list:numbers) on the source database.

The script then pops these numbers from the replica database to verify replication.

Running the Script

Execute the script using:

chmod +x replication_test.sh
./replication_test.sh

Expected Output

Confirmation that numbers were successfully added to the source database.

Confirmation that numbers were retrieved from the replica database.

Troubleshooting

If replication does not work, ensure the source and replica databases are correctly configured.

Check the Redis logs to verify that replication is active.

Use redis-cli to manually inspect the list:numbers on both databases.

License

This project is licensed under the MIT License.

