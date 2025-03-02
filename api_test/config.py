# config.py

BASE_URL = "https://172.16.22.21:9443/v1"
USERNAME = "admin@rl.org"
PASSWORD = "mkZGAIu"

ROLES = ["db_viewer", "db_member"]

DB_NAME = "database1"

USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer"},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member"},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin"}
]
