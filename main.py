import os
import subprocess
import redis_api.config as config
from redis_api.redis_api_test import RedisAPI

def run_replication_test():
    subprocess.run(['bash', os.path.join(os.path.dirname(__file__), 'replication_test', 'replication_test.sh')])

def run_redis_api_test():
    try:
        redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        redis_api.run_all()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        return

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
