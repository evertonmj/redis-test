import requests
from requests.auth import HTTPBasicAuth
import urllib3
import config  # Importa o arquivo de configuração

# Desativar avisos de certificado inseguro
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RedisAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)

    def _make_request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, auth=self.auth, json=data, verify=False)
        if response.status_code in [200, 201]:
            return response.json()
        else:
            print(f"Error {method} {endpoint}: {response.status_code}")
            print(response.text)
            return None

    def create_role(self, role_name):
        data = {"name": role_name}
        return self._make_request("POST", "/roles", data)

    def create_database(self, db_name, max_memory):
        data = {"name": db_name, "memory_size": max_memory}
        return self._make_request("POST", "/bdbs", data)

    def create_user(self, user):
        data = {"email": user['email'], "name": user['name'], "role": user['role'], "password": user['password']}
        return self._make_request("POST", "/users", data)

    def list_users(self):
        users = self._make_request("GET", "/users")
        if users:
            for user in users:
                print(f"Name: {user['name']}, Role: {user['role']}, Email: {user['email']}")
        return users

    def delete_database(self, db_uid):
        if not db_uid:
            print("Database UID not found, skipping deletion.")
            return
        return self._make_request("DELETE", f"/bdbs/{db_uid}")

# Instanciar API
redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)

# Criar roles necessários
for role in config.ROLES:
    redis_api.create_role(role)

# Criar banco de dados
db_info = redis_api.create_database(config.DB_NAME, config.DB_MAX_MEMORY)

db_uid = db_info.get("uid") if db_info else None

# Criar usuários
for user in config.USERS:
    redis_api.create_user(user)

# Listar usuários
redis_api.list_users()

# Deletar banco de dados
redis_api.delete_database(db_uid)
