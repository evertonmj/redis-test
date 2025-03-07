# Redis API Client

## Overview
This Python script provides a complete interface to interact with a Redis API. It automates the management of roles, databases, and users, offering functionalities such as:

- **Create a New Database**: Utilize the Database API to create a new database without using any modules.
- **Create Three New Users**: Utilize the Users API to add three new users to the system with the following details:
  - Email: john.doe@example.com, Name: John Doe, Role: db_viewer
  - Email: mike.smith@example.com, Name: Mike Smith, Role: db_member
  - Email: cary.johnson@example.com, Name: Cary Johnson, Role: admin
- **List and Display Users**: Utilize the Users API to fetch and display all users in the specified format (name, role, and email).
- **Delete the Created Database**: Use the Database API to delete the previously created database.

## Features
- **Secure API Requests**: Uses `requests` with `HTTPBasicAuth` for authentication.
- **Error Handling**: Detects connection failures, invalid requests, and authentication errors.
- **Configuration Management**: Uses a separate `config.py` file for parameters and API settings.
- **Automated Execution**: The script runs all operations in sequence.

## Prerequisites
- Python 3.x and PIP 3.x installed on your system.
- `redis-cli` tool installed on your system.

### Dependencies
```bash
pip install requests urllib3
```

## Configuration
The script relies on a `config.py` file to store API connection details and default values. 

### Example `config.py` File:
```python
# config.py

# Redis API Configuration
BASE_URL = "https://your-redis-api-url/v1"
USERNAME = "your-admin-username"
PASSWORD = "your-admin-password"

# Redis Roles
ROLES = [
    {
        "name": "db_viewer",
        "management": "db_viewer"
    }, {
        "name": "db_member",
        "management": "db_member"
    }
]

# Redis Database Configuration
DB_NAME = "database1"
DB_MAX_MEMORY = 1073741824  # 1GB

USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer", "password": "securePass123"},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member", "password": "securePass123"},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin", "password": "securePass123"}
]
```

## Running the Script
To execute all operations automatically, run:

```bash
python redis_api.py
```

Alternatively, you can import the `RedisAPI` class in another script and call its methods individually.

```python
from redis_api import RedisAPI
import config

redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
redis_api.create_database("new_db", 2147483648)  # Creates a 2GB database
```

## Available Methods
The `RedisAPI` class provides the following methods:

### `create_role(role)`
Creates a new role in Redis.
- **Input:** A dictionary with `name`.
- **Example:**
  ```python
  redis_api.create_role({"name": "db_reader"})
  ```

### `create_database(db_name, max_memory)`
Creates a new Redis database with the specified name and memory limit.
- **Input:**
  - `db_name`: String (Database Name)
  - `max_memory`: Integer (Memory in Bytes)
- **Example:**
  ```python
  redis_api.create_database("my_database", 1073741824)
  ```

### `create_user(user)`
Creates a new user with the specified email, name, role, and password.
- **Input:** A dictionary with `email`, `name`, `role`, and `password`.
- **Example:**
  ```python
  redis_api.create_user({"email": "jane.doe@example.com", "name": "Jane Doe", "role": "db_member", "password": "securePass123"})
  ```

### `list_users()`
Lists all registered users in Redis.
- **Example:**
  ```python
  redis_api.list_users()
  ```

### `delete_database(db_uid)`
Deletes the database specified by its unique ID.
- **Input:**
  - `db_uid`: Integer (Database UID)
- **Example:**
  ```python
  redis_api.delete_database(12)
  ```

## Error Handling
The script is designed to handle errors efficiently:

- **HTTP errors:** Detects authentication failures and invalid requests.
- **Connection issues:** Handles network failures and server downtimes.
- **Missing parameters:** Ensures required values are provided before making API calls.
- **Invalid input data:** Prevents incorrect data from being sent to the API.

## Expected Output
Upon execution, the script logs the following messages:

- **Success Messages:**
  ```bash
  Success: POST /roles - Status Code: 200
  Role 'db_viewer' created successfully.
  ```

- **Error Messages:**
  ```bash
  HTTP error occurred: 401 Client Error: Unauthorized for url
  ```

## Troubleshooting
- **Issue: No response from the API**
  - Ensure the API server is running and reachable.
  - Check `BASE_URL` in `config.py`.

- **Issue: Authentication failure**
  - Verify `USERNAME` and `PASSWORD` in `config.py`.
  - Ensure the credentials have the necessary API permissions.

- **Issue: Users or roles not appearing**
  - Check for existing roles before creating them.
  - Run `list_users()` to confirm user creation.

## License
This project is licensed under the MIT License.

