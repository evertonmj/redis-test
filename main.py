import os
import subprocess
import rest_api_test.config as config
from rest_api_test.redis_api_test import RedisAPI

def run_replication_test():
    subprocess.run(['bash', os.path.join(os.path.dirname(__file__), 'replication_test', 'replication_test.sh')])

def run_redis_api_test():
    while True:
        print("\nChoose a Redis API test to run:")
        print("1. Run All Redis API Tests")
        print("2. Run Create Role Test")
        print("3. Run Create Database Test")
        print("4. Run Create User Test")
        print("5. Run List Users Test")
        print("6. Run Delete Database Test")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
                redis_api.run_all()
            except ValueError as e:
                print(f"Configuration Error: {e}")
        elif choice == "2":
            run_create_role_test()
        elif choice == "3":
            db_uid = run_create_database_test()
        elif choice == "4":
            run_create_user_test()
        elif choice == "5":
            run_list_users_test()
        elif choice == "6":
            db_delete = input("Enter database UID: ")
            run_delete_database_test(db_delete)
            print("No database UID available. Please run the Create Database Test first.")
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

def run_create_role_test():
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        redis_api.run_create_role_test()
    except ValueError as e:
        print(f"Configuration Error: {e}")

def run_create_database_test():
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        db_uid = redis_api.run_create_database_test()
        return db_uid
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return None

def run_create_user_test():
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        redis_api.run_create_user_test()
    except ValueError as e:
        print(f"Configuration Error: {e}")

def run_list_users_test():
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        redis_api.run_list_users_test()
    except ValueError as e:
        print(f"Configuration Error: {e}")

def run_delete_database_test(db_uid):
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        redis_api.run_delete_database_test(db_uid)
    except ValueError as e:
        print(f"Configuration Error: {e}")

def main():
    db_uid = None
    while True:
        print("\nChoose a test to run:")
        print("1. Run Replication Test")
        print("2. Redis REST API Test")
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
