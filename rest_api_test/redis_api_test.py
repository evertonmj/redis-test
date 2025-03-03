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
        return response.get('uid')

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
        
        data = {"uid": db_uid, "crdt_sync": "disabled"}
        flushResponse = self._make_request("PUT", f"/bdbs/{db_uid}", data)

        response = self._make_request("DELETE", f"/bdbs/{db_uid}")
        if response:
            print(f"Database with UID {db_uid} deleted successfully.")
        else:
            print(f"Retry Database with UID {db_uid} deletion.")
            for i in range(3):
                print(f"Retry Database with UID {db_uid} deletion. #{i}")
                flushResponse = self._make_request("PUT", f"/bdbs/{db_uid}", data)
                response = self._make_request("DELETE", f"/bdbs/{db_uid}")


    def run_all(self):
        try:
            redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
        except ValueError as e:
            print(f"Configuration Error: {e}")
            exit(1)

        for role in config.ROLES:
            redis_api.create_role(role)

        db_uid = redis_api.create_database(config.DB_NAME, config.DB_MAX_MEMORY)

        for user in config.USERS:
            redis_api.create_user(user)

        redis_api.list_users()

        redis_api.delete_database(db_uid)

    if __name__ == "__main__":
        run_all()
