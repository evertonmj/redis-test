# Redis Testing Suite

## Overview
This project provides a comprehensive testing framework for Redis, including:
- **Replication Testing**: Ensures data consistency across Redis replicas.
- **Redis API Testing**: Automates the creation and management of databases, roles, and users via a Redis API.

The suite includes:
1. **Replication Test** (`replication_test.sh`): Simulates data insertion in a source Redis instance and verifies replication in a replica.
2. **Redis API Test** (`redis_api_test.py`): Automates API-based Redis management, including database creation, user management, and role assignment.
3. **Main Script** (`main.py`): A CLI interface to run either of the above tests.

## Prerequisites
Before running the tests, install the required dependencies:

```bash
pip install requests urllib3
```

Ensure Redis CLI is installed for replication tests:
```bash
sudo apt install redis-tools  # Debian/Ubuntu
brew install redis  # macOS
```

## Environment Variables

Set up the following environment variables in a `.env` file or export them in your shell:

```properties
export REDIS_BASE_URL=[[YOUR_ENDPOINT]]
export API_USERNAME=[[YOUR_USER]]
export API_PASSWORD=[[YOUR_PASS]]
export SOURCE_DATABASE_HOST=[[SOURCE_DB]]
export REPLICA_DATABASE_HOST=[[REPLICA_DB]]

```

## Configuration


The framework relies on a `config.py` file to store environment-specific parameters. Create `config.py` in the `rest_api_test` directory:

```python
# config.py

BASE_URL = "https://your-redis-api-url/v1"
USERNAME = "your-admin-username"
PASSWORD = "your-admin-password"

ROLES = [
    {"name": "db_viewer"},
    {"name": "db_member"}
]

DB_NAME = "test_database"
DB_MAX_MEMORY = 1073741824  # 1GB

USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer", "password": "securePass123"},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member", "password": "securePass123"},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin", "password": "securePass123"}
]
```

## Running Tests
To execute the testing framework, run:
```bash
python main.py
```
You will be prompted to choose a test:
1. Replication Test
2. Redis API Test
3. Exit

### Running Tests Individually
#### Replication Test
Manually run the replication test:
```bash
bash replication_test/replication_test.sh
```

#### Redis API Test
Execute the Redis API test independently:
```bash
python -m rest_api_test.redis_api_test
```

## Troubleshooting
- **Replication Not Working?**
  - Ensure both source and replica Redis instances are properly configured.
  - Check `redis-cli info replication` on both nodes.

- **API Authentication Failure?**
  - Verify credentials in `config.py`.
  - Ensure the API server is running and accessible.

- **Users or Roles Not Appearing?**
  - Confirm that roles exist before assigning them to users.
  - Run `list_users()` to check user creation.

## License
This project is licensed under the MIT License.

