# Redis API Automation

## Overview
This Python script automates the process of managing a Redis database via API.

## Prerequisites
Ensure you have the following dependencies installed:

```bash
pip install requests urllib3
```

## Configuration
The script uses a `config.py` file to store important parameters. Create a `config.py` file in the same directory with the following content:

```python
# config.py

import os

BASE_URL = os.getenv("REDIS_BASE_URL", "https://your-redis-api-url/v1")
USERNAME = os.getenv("API_USERNAME", "your-admin-username")
PASSWORD = os.getenv("API_PASSWORD", "your-admin-password")

ROLES = [
    {"name": "db_viewer"},
    {"name": "db_member"}
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

## Running the Script
Execute the script using Python:

```bash
python redis_api_test.py
```

## Expected Output
The script will:

1. Create the required roles (`db_viewer`, `db_member`)
2. Create a Redis database
3. Create users
4. List all users
5. Delete the created database

## Error Handling
The script includes error handling for:

- API connection failures
- Missing required parameters
- Invalid response handling

## License
This project is licensed under the MIT License.

