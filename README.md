# Redis Test

## Overview
This project provides tools and scripts for managing and testing Redis databases. It includes:

1. **Replication Test**: A script to test Redis replication and verify data synchronization between primary and replica databases.
2. **API Test**: A Python script to automate Redis database management via a REST API, including creating databases, users, and roles.

## Replication Test

The replication test script verifies data synchronization between a primary Redis database and its replica. This ensures that changes made in the primary database are correctly reflected in the replica.

### Instructions

1. Set up and run the test by following the steps in [replication_test/README.md](replication_test/README.md).
2. Ensure both the primary and replica databases are properly configured.
3. Verify that data inserted into the primary database is replicated to the replica database.

## API Test

The API test script automates the process of managing Redis databases via a REST API. It allows operations such as:
- Creating and deleting databases.
- Managing roles and permissions.
- Creating, updating, and deleting users.
- Listing registered users in Redis.

### Instructions

1. Set up and run the API test by following the steps in [api_test/README.md](api_test/README.md).
2. Ensure the API is available and accessible.
3. Verify that data managed through the API is correctly reflected in the Redis system.

## Prerequisites
To run the test scripts correctly, ensure you meet the following requirements:

- Redis Enterprise installed and properly configured.
- Python 3.x installed on your system.
- Install required dependencies:

```bash
pip install requests urllib3
```

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
- Use the `list_users()` function in the API test script to verify registered users.

## License
This project is licensed under the MIT License.

