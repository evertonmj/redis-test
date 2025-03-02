import os

# config.py

BASE_URL = os.getenv("REDIS_BASE_URL", "REST_API_ENDPOINT")
USERNAME = os.getenv("API_USERNAME", "user")
PASSWORD = os.getenv("API_PASSWORD", "pass")

DB_NAME = "ever-database-01"
DB_MAX_MEMORY = 1073741824

USER_DEFAULT_PASSWORD = "twinpeaks2402"
USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer", "password": USER_DEFAULT_PASSWORD},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member",  "password": USER_DEFAULT_PASSWORD},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin", "password": USER_DEFAULT_PASSWORD}
]

ROLES = [
    {
        "name": "db_viewer",
        "management": "db_viewer"
    }, {
        "name": "db_member",
        "management": "db_member"
    }
]
