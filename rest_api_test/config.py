import os

# config.py
# This is a configuration file that contains the settings for the Redis API test.
# You can customize these settings based on your environment.
# You can also set these values as environment variables.

# About the settings:
# BASE_URL: The base URL of the Redis API.
# USERNAME: The username for the Redis API authentication.
# PASSWORD: The password for the Redis API authentication.
# DB_NAME: The name of the Redis database to be created.
# DB_MAX_MEMORY: The maximum memory limit for the Redis database.
# USER_DEFAULT_PASSWORD: The default password for new users.
# USERS: A list of user objects with email, name, role, and password.
# ROLES: A list of role objects with name and management.

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
