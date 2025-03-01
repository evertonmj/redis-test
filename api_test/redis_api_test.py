import json
import requests
import os

BASE_URL = os.environ['REST_API_ENDPOINT']
HEADERS = {"Content-Type": "application/json"}

def create_database():
    url = f"{BASE_URL}/databases"
    payload = json.dumps({"name": "test_db"})
    response = requests.post(url, data=payload, headers=HEADERS, verify=False)
    
    if response.status_code == 201:
        db_id = response.json().get("id")
        print(f"Database created with ID: {db_id}")
        return db_id
    else:
        print("Failed to create database:", response.text)
        return None

def create_user(email, name, role):
    url = f"{BASE_URL}/users"
    payload = json.dumps({"email": email, "name": name, "role": role})
    response = requests.post(url, data=payload, headers=HEADERS, verify=False)
    
    if response.status_code == 201:
        print(f"User {name} created successfully.")
    else:
        print(f"Failed to create user {name}:", response.text)

def list_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url, headers=HEADERS, verify=False)
    
    if response.status_code == 200:
        users = response.json()
        print("\nUsers in the system:")
        for user in users:
            print(f"Name: {user['name']}, Role: {user['role']}, Email: {user['email']}")
    else:
        print("Failed to retrieve users:", response.text)

def delete_database(db_id):
    url = f"{BASE_URL}/databases/{db_id}"
    response = requests.delete(url, headers=HEADERS, verify=False)
    
    if response.status_code == 200:
        print("Database deleted successfully.")
    else:
        print("Failed to delete database:", response.text)

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
