# Redis Project

This project contains scripts and tools for managing and testing Redis databases. It includes:

1. **Replication Test**: A script to test Redis database replication.
2. **API Test**: A Python script to automate Redis database management via REST API.

## Replication Test

The replication test script helps you set up and verify Redis replication between two databases.

### Instructions

1. Follow the steps in the [replication_test/README.md](replication_test/README.md) to set up and run the replication test.

### Detailed Instructions

#### 1. Create Source Database

Create a single-sharded Redis Enterprise database named `source-db` with no password and a memory limit of 2GB. You can learn how to create Redis Enterprise databases [here](https://docs.redislabs.com/latest/rs/administering/creating-databases/).

#### 2. Enable Replica Of

Create another single-sharded Redis Enterprise database named `replica-db` with no password and a memory limit of 2GB. Use `source-db` as the source database.

#### 3. Connect on the bastion host using the link on doc page

#### 4. Install and configure tools:

##### 4.1 Update package manager
```sh
apk update && apk upgrade 
apk add --update alpine-sdk
```

##### 4.2 Install git, bash and compiling tools
```sh
apk add --no-cache bash git openssh make cmake python3
pip3 install requests
```

##### 4.3 Get redis source code
```sh
wget http://download.redis.io/redis-stable.tar.gz
```

##### 4.4 Unpack and compile redis
```sh
tar xvzf redis-stable.tar.gz
cd redis-stable
make redis-cli
```

##### 4.5 Copy Redis executable
```sh
sudo cp src/redis-cli /usr/local/bin/
```

##### 4.6 Connect to source database and insert value

###### 4.6.1 Connect to source db node: 
```sh
redis-cli -u redis://<SOURCE_DB_ENDPOINT>:<SOURCE_DB_PORT>
```

###### 4.6.2 Insert value
```sh
SET test:tb:1 "test ok"
```

##### 4.7 Connect to replica database and check if value is inserted

###### 4.7.1 Connect to replica db node: 
```sh
redis-cli -u redis://<REPLICA_DB_ENDPOINT>:<REPLICA_DB_PORT>
```

###### 4.7.2 Check if value is inserted
```sh
GET test:tb:1
```

#### 5. Run test case ###

##### 5.1 Set environment variables

Set the environment variables for the source and replica databases:
```sh
export SOURCE_DATABASE_HOST=<SOURCE_DB_ENDPOINT>:<SOURCE_DB_PORT>
export REPLICA_DATABASE_HOST=<REPLICA_DB_ENDPOINT>:<REPLICA_DB_PORT>
```

##### 5.2 Download test script
```sh
wget https://raw.githubusercontent.com/evertonmj/redis-test/refs/heads/main/replication_test.sh
```

##### 5.3 Execute
```sh
sh replication_test.sh
```

### Expected Output

The script will:
1. Push numbers from 1 to 100 to the source database.
2. Pop numbers from the replica database.

## API Test

The API test script automates the process of managing Redis databases, including creating roles, databases, and users.

### Instructions

1. Follow the steps in the [api_test/README.md](api_test/README.md) to configure and run the API test script.

### Detailed Instructions

#### Prerequisites
Ensure you have the following dependencies installed:

```bash
pip install requests urllib3
```

#### Configuration
The script uses a `config.py` file to store important parameters. Create a `config.py` file in the same directory with the following content:

```python
# config.py

import os

BASE_URL = os.getenv("REDIS_BASE_URL", "https://your-redis-api-url/v1")
USERNAME = os.getenv("API_USERNAME", "your-admin-username")
PASSWORD = os.getenv("API_PASSWORD", "your-admin-password")

ROLES = [
    {"name": "db_viewer", "management": "db_viewer"},
    {"name": "db_member", "management": "db_member"}
]

DB_NAME = "database1"
DB_MAX_MEMORY = 1073741824  # 1GB

USER_DEFAULT_PASSWORD = "securePass123"
USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer", "password": USER_DEFAULT_PASSWORD},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member", "password": USER_DEFAULT_PASSWORD},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin", "password": USER_DEFAULT_PASSWORD}
]
```

#### Running the Script
Execute the script using Python:

```bash
python redis_api_test.py
```

### Expected Output
The script will:

1. Create the required roles (`db_viewer`, `db_member`)
2. Create a Redis database
3. Create users
4. List all users
5. Delete the created database

### Error Handling
The script includes error handling for:

- API connection failures
- Missing required parameters
- Invalid response handling

## Prerequisites

- Redis Enterprise installed and configured
- Python 3.x installed
- Required Python packages: `requests`, `urllib3`

## Environment Variables

Set up the following environment variables in a `.env` file or export them in your shell:

```properties
export REDIS_BASE_URL=[[YOUR_ENDPOINT]]
export API_USERNAME=[[YOUR_USER]]
export API_PASSWORD=[[YOUR_PASS]]
export SOURCE_DATABASE_HOST=[[SOURCE_DB]]
export REPLICA_DATABASE_HOST=[[REPLICA_DB]]

```

## License

This project is licensed under the MIT License.
