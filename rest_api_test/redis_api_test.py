import requests
from requests.auth import HTTPBasicAuth
import urllib3
import rest_api_test.config as config


# disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RedisAPI:
    def __init__(self, base_url, username, password):
        if not base_url or not username or not password:
            raise ValueError("Missing required API configuration parameters.")
        
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)

    def _make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, auth=self.auth, json=data, verify=False)
            response.raise_for_status()
            print(f"Success: {method} {endpoint} - Status Code: {response.status_code}")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - Response: {response.text}")
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
        return None

    def create_role(self, role):
        if "name" not in role or not role["name"]:
            print("Invalid role data. 'name' is required.")
            return
        response = self._make_request("POST", "/roles", role)
        if response:
            print(f"Role '{role['name']}' created successfully.")

    def create_database(self, db_name, max_memory):
        if not db_name or not isinstance(max_memory, int) or max_memory <= 0:
            print("Invalid database parameters.")
            return None
        data = {"name": db_name, "memory_size": max_memory}
        response = self._make_request("POST", "/bdbs", data)
        if response:
            print(f"Database '{db_name}' created successfully with UID {response.get('uid')}.")
        return response

    def create_user(self, user):
        required_keys = ["email", "name", "role", "password"]
        if not all(key in user and user[key] for key in required_keys):
            print("Invalid user data. 'email', 'name', 'role', and 'password' are required.")
            return
        response = self._make_request("POST", "/users", user)
        if response:
            print(f"User '{user['name']}' created successfully.")

    def list_users(self):
        users = self._make_request("GET", "/users")
        if users:
            print("Registered Users:")
            for user in users:
                print(f"- Name: {user['name']}, Role: {user['role']}, Email: {user['email']}")
        return users

    def delete_database(self, db_uid):
        if not db_uid:
            print("Database UID not found, skipping deletion.")
            return
        response = self._make_request("DELETE", f"/bdbs/{db_uid}")
        if response:
            print(f"Database with UID {db_uid} deleted successfully.")

    def run_create_role_test(self):
        for role in config.ROLES:
            self.create_role(role)

    def run_create_database_test(self):
        db_info = self.create_database(config.DB_NAME, config.DB_MAX_MEMORY)
        return db_info.get("uid") if db_info else None

    def run_create_user_test(self):
        for user in config.USERS:
            self.create_user(user)

    def run_list_users_test(self):
        self.list_users()

    def run_delete_database_test(self, db_uid):
        self.delete_database(db_uid)

    def run_all(self):
        try:
            redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        except ValueError as e:
            print(f"Configuration Error: {e}")
            exit(1)

        redis_api.run_create_role_test()
        db_uid = redis_api.run_create_database_test()
        redis_api.run_create_user_test()
        redis_api.run_list_users_test()
        redis_api.run_delete_database_test(db_uid)

    if __name__ == "__main__":
        run_all()
