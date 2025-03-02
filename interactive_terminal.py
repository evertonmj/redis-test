import os
import subprocess
import redis_api.config
from redis_api.redis_api_test import RedisAPI

def run_replication_test():
    script_path = os.path.join(os.path.dirname(__file__), 'replication_test', 'replication-test.sh')
    subprocess.run(['bash', script_path])

def run_redis_api_test():
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return

    while True:
        print("\nChoose an option:")
        print("1. Create Role")
        print("2. Create Database")
        print("3. Create User")
        print("4. List Users")
        print("5. Delete Database")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            role_name = input("Enter role name: ")
            role_management = input("Enter role management: ")
            role = {"name": role_name, "management": role_management}
            redis_api.create_role(role)
        elif choice == "2":
            db_name = input("Enter database name: ")
            max_memory = int(input("Enter max memory (in bytes): "))
            redis_api.create_database(db_name, max_memory)
        elif choice == "3":
            email = input("Enter user email: ")
            name = input("Enter user name: ")
            role = input("Enter user role: ")
            password = input("Enter user password: ")
            user = {"email": email, "name": name, "role": role, "password": password}
            redis_api.create_user(user)
        elif choice == "4":
            redis_api.list_users()
        elif choice == "5":
            db_uid = input("Enter database UID to delete: ")
            redis_api.delete_database(db_uid)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    while True:
        print("\nChoose a test to run:")
        print("1. Run Replication Test")
        print("2. Run Redis API Test")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            run_replication_test()
        elif choice == "2":
            run_redis_api_test()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
