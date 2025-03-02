# Redis Test

## Overview
In this project some Redis Enterprise features are tested and validated. It includes:

**Datbases Replication Test**: A script to test Redis database replication and verify data synchronization between primary and replica databases.

**REST API Test**: A Python script to automate Redis database management via its REST API, including creatin and management of databases, users, and roles.

------------

0. ## Before Running the Scripts

## Requirements
* You must have a Redis Enterprise Account. You can try it for free here: [Try it for free](https://redis.io/try-free/). After getting access to your account, you will need credentials (user/password) to interact with the API.

* You must have access to a computer terminal. If you are using Microsoft Windows, [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5) is highly recommended.

* Basic programming skills and how to use a computer terminal to interact with external services.

* For the purposes of this test, a Bastion Host was available to connect and interact with Redis Services. Please, ask for support about how can you get ready to connect and interact with your cluster.

1. ## Running Interactively

You can perform this tests by running the main python script (main.py) or by running individual test script.

- Before running, it's important to ensure that you have connectivity to your cluster. For example, private VPC endpoints will work only if you are connected to you cluster.

- To run main script: `python main.py`

2. ## Database Replication Test

The replication test script verifies data synchronization between a primary Redis database and its replica. This ensures that changes made in the primary database are correctly reflected in the replica.

This script was written in pure *nix bash and redis-cli tool. For more information on using the Redis CLI, refer to the [official documentation](https://redis.io/docs/latest/develop/tools/cli/).

### Instructions

1. Set up and run the test by following the steps in [replication_test/README.md](replication_test/README.md).
2. Ensure both the primary and replica databases are properly configured.
3. Verify that data inserted into the primary database is replicated to the replica database.

2. ## REST API Test

The API test script automates the process of managing Redis databases via a REST API. It executes the following operations:
- Creating and deleting databases.
- Managing roles and permissions.
- Creating, updating, and deleting users.
- Listing registered users in Redis.

### Instructions

1. Set up and run the API test by following the steps in [api_test/README.md](api_test/README.md).
2. Ensure the API is available and accessible.
3. Verify that data managed through the API is correctly reflected in the Redis system. Yous can check it at Redis Enterprise main dashboard

## Prerequisites
To run the test scripts correctly, ensure you meet the following requirements:

- Redis Enterprise account.
- Rest API enabled
- Redis credentials
- Python and PIP 3.x installed. If you use a bastion host, these tools must be installed there.

## Environment Variables
Before running the scripts, set up the following environment variables in a `.env` file or export them in the terminal:

```properties
export REDIS_BASE_URL=[[YOUR_ENDPOINT]]
export API_USERNAME=[[YOUR_USER]]
export API_PASSWORD=[[YOUR_PASSWORD]]
export SOURCE_DATABASE_HOST=[[SOURCE_DB_HOST]]
export REPLICA_DATABASE_HOST=[[REPLICA_DB_HOST]]
```

If using a `.env` file, load it into the session before executing the scripts:

```bash
source .env
```

## Troubleshooting
### 1. Replication is not working
- Ensure the primary and replica databases are correctly configured.
- Use the command `redis-cli info replication` to check replication status.

### 2. Unable to access the API
- Ensure the API URL (`REDIS_BASE_URL`) in `config.py` is correct.
- Verify that the credentials (`API_USERNAME`, `API_PASSWORD`) are valid.
- Check that the API server is running.

### 3. Users or roles do not appear in Redis
- Ensure that roles are created before assigning them to users.

## License
This project is licensed under the MIT License.

