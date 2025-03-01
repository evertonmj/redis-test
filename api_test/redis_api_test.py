import requests
import json
import ssl

# Configurações do Redis REST API com autenticação via certificado
REDIS_API_URL = "https://your-redis-server:8080/v1"
CERT_PATH = "certfile.pem"
KEY_PATH = "cert.key"  # Remova esta linha se não precisar de chave
VERIFY_SSL = True  # Altere para False se quiser desativar a verificação SSL
HEADERS = {"Content-Type": "application/json"}

# Testa se a chave privada existe e é necessária
USE_PRIVATE_KEY = False
try:
    with open(KEY_PATH, "r") as key_file:
        USE_PRIVATE_KEY = True
except FileNotFoundError:
    print("[INFO] Chave privada não encontrada, tentando apenas com o certificado.")


def create_database(database_name):
    url = f"{REDIS_API_URL}/databases"
    data = {"name": database_name}
    cert = (CERT_PATH, KEY_PATH) if USE_PRIVATE_KEY else CERT_PATH
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(data), cert=cert, verify=VERIFY_SSL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.SSLError as e:
        print("[ERROR] Erro SSL:", e)
    except requests.exceptions.RequestException as e:
        print("[ERROR] Erro na requisição:", e)
    return None


def set_key(database, key, value):
    url = f"{REDIS_API_URL}/databases/{database}/keys/{key}"
    data = {"value": value}
    cert = (CERT_PATH, KEY_PATH) if USE_PRIVATE_KEY else CERT_PATH
    response = requests.put(url, headers=HEADERS, data=json.dumps(data), cert=cert, verify=VERIFY_SSL)
    return response.json()


def get_key(database, key):
    url = f"{REDIS_API_URL}/databases/{database}/keys/{key}"
    cert = (CERT_PATH, KEY_PATH) if USE_PRIVATE_KEY else CERT_PATH
    response = requests.get(url, headers=HEADERS, cert=cert, verify=VERIFY_SSL)
    if response.status_code == 200:
        return response.json()
    return None


def delete_key(database, key):
    url = f"{REDIS_API_URL}/databases/{database}/keys/{key}"
    cert = (CERT_PATH, KEY_PATH) if USE_PRIVATE_KEY else CERT_PATH
    response = requests.delete(url, headers=HEADERS, cert=cert, verify=VERIFY_SSL)
    return response.json()


if __name__ == "__main__":
    database = "mydatabase"
    key = "username"
    value = "Everton"
    
    print("Criando banco de dados no Redis...")
    db_response = create_database(database)
    if db_response:
        print(db_response)
    else:
        print("[ERROR] Falha ao criar banco de dados.")
        exit()
    
    print("Salvando dado no Redis...")
    print(set_key(database, key, value))
    
    print("Recuperando dado do Redis...")
    print(get_key(database, key))
    
    print("Deletando dado do Redis...")
    print(delete_key(database, key))
