import requests
from requests.auth import HTTPBasicAuth
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def create_role(base_url, auth, role_name, role_management):
    url = f"{base_url}/roles"
    data = {"name": role_name, "management": role_management}
    response = requests.post(url, auth=auth, json=data, verify=False)
    if response.status_code == 200:
        print(f"Role created - Name: {role_name} / ID: {response.json().get('uid')}")
    else:
        print("Error creating role")

def create_database(base_url, auth, db_name):
    url = f"{base_url}/bdbs"
    data = {"name": db_name, "memory_size": 1073741824}
    response = requests.post(url, auth=auth, json=data, verify=False)
    
    if response.status_code == 200:
        db_info = response.json()
        print(f"Database created - Name: {db_info['name']}, UID: {db_info['uid']}")
    else:
        print("Error creating database")

    return response.json().get("uid") if response.status_code == 200 else None

def create_user(base_url, auth, email, name, role, password="defaultPass123"):
    url = f"{base_url}/users"
    data = {"email": email, "name": name, "role": role, "password": password}
    response = requests.post(url, auth=auth, json=data, verify=False)
    if response.status_code == 200:
        user = response.json()
        print(f"User Created - ID: {user['uid']}, Name: {user['name']}")
    else:
        print("Error creating user")

def list_users(base_url, auth):
    url = f"{base_url}/users"
    response = requests.get(url, auth=auth, verify=False)
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(f"Name: {user['name']}, Role: {user['role']}, Email: {user['email']}")
    else:
        print("Error")

def delete_database(base_url, auth, db_uid):
    if not db_uid:
        print("Database UID not found, skipping deletion.")
        return
    url = f"{base_url}/bdbs/{db_uid}"
    response = requests.delete(url, auth=auth, verify=False)
    print("Delete Database Status:", response.status_code)

# Definição da URL e credenciais
base_url = "https://172.16.22.21:9443/v1"
auth = HTTPBasicAuth("admin@rl.org", "mkZGAIu")

# Criar roles necessários
roles = [
    {
        "name": "db_viewer",
        "management": "db_viewer"
    }, {
        "name": "db_member",
        "management": "db_member"
    }
]

for role in roles:
    create_role(base_url, auth, role['name'], role['management'])

db_name = "ever-db-01"
db_uid = create_database(base_url, auth, db_name)

users = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer"},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member"},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin"}
]

for user in users:
    create_user(base_url, auth, user['email'], user['name'], user['role'])

list_users(base_url, auth)

delete_database(base_url, auth, db_uid)