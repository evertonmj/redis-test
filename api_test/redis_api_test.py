import json
import requests
import os

# Configurações de ambiente
BASE_URL = os.environ.get('REST_API_ENDPOINT')  # Fallback caso a variável não esteja definida
CA_CERT_PATH = os.environ.get('CA_CERT_PATH')  # Caminho do certificado CA

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Host": BASE_URL
}

print(f"Using API Endpoint: {BASE_URL}")

# Apenas verificação do certificado CA
VERIFY = CA_CERT_PATH if CA_CERT_PATH else True  # False para testes (não recomendado)

def create_database():
    url = f"{BASE_URL}/databases"
    payload = json.dumps({"host": BASE_URL})
    
    try:
        response = requests.post(url, data=payload, headers=HEADERS, verify=VERIFY)
        response.raise_for_status()
        db_id = response.json().get("id")
        print(f"Database created with ID: {db_id}")
        return db_id
    except requests.exceptions.RequestException as e:
        print(f"Failed to create database: {e}")
        return None

def create_user(email, name, role):
    url = f"{BASE_URL}/users"
    payload = json.dumps({"email": email, "name": name, "role": role})
    
    try:
        response = requests.post(url, data=payload, headers=HEADERS, verify=VERIFY)
        response.raise_for_status()
        print(f"User {name} created successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to create user {name}: {e}")

def list_users():
    url = f"{BASE_URL}/users"
    
    try:
        response = requests.get(url, headers=HEADERS, verify=VERIFY)
        response.raise_for_status()
        users = response.json()
        print("\nUsers in the system:")
        for user in users:
            print(f"Name: {user['name']}, Role: {user['role']}, Email: {user['email']}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve users: {e}")

def delete_database(db_id):
    url = f"{BASE_URL}/databases/{db_id}"
    
    try:
        response = requests.delete(url, headers=HEADERS, verify=VERIFY)
        response.raise_for_status()
        print("Database deleted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete database: {e}")

def main():
    db_id = create_database()
    if db_id:
        create_user("john.doe@example.com", "John Doe", "db_viewer")
        create_user("mike.smith@example.com", "Mike Smith", "db_member")
        create_user("cary.johnson@example.com", "Cary Johnson", "admin")
        list_users()
        delete_database(db_id)

if __name__ == "__main__":
    main()
