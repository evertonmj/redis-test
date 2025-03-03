# Cliente de API de Redis

## Descripción general
Este script en Python proporciona una interfaz completa para interactuar con una API de Redis. Automatiza la gestión de roles, bases de datos y usuarios, ofreciendo funcionalidades como:

- **Crear una nueva base de datos**: Utiliza la API de bases de datos para crear una nueva base de datos sin usar módulos adicionales.
- **Crear tres nuevos usuarios**: Utiliza la API de usuarios para agregar tres nuevos usuarios al sistema con los siguientes detalles:
  - Correo: john.doe@example.com, Nombre: John Doe, Rol: db_viewer
  - Correo: mike.smith@example.com, Nombre: Mike Smith, Rol: db_member
  - Correo: cary.johnson@example.com, Nombre: Cary Johnson, Rol: admin
- **Listar y mostrar usuarios**: Usa la API de usuarios para obtener y mostrar todos los usuarios en el formato especificado (nombre, rol y correo electrónico).
- **Eliminar la base de datos creada**: Usa la API de bases de datos para eliminar la base de datos creada previamente.

## Características
- **Solicitudes API seguras**: Utiliza `requests` con `HTTPBasicAuth` para autenticación.
- **Manejo de errores**: Detecta fallos de conexión, solicitudes inválidas y errores de autenticación.
- **Gestión de configuración**: Usa un archivo `config.py` separado para los parámetros y configuraciones de la API.
- **Ejecución automatizada**: El script ejecuta todas las operaciones en secuencia.

## Requisitos previos
- Python 3.x y PIP 3.x instalados en tu sistema.
- Herramienta `redis-cli` instalada en tu sistema.

### Dependencias
```bash
pip install requests urllib3
```

## Configuración
El script usa un archivo `config.py` para almacenar los detalles de conexión a la API y los valores predeterminados.

### Ejemplo de archivo `config.py`:
```python
# config.py

# Configuración de la API de Redis
BASE_URL = "https://tu-api-redis-url/v1"
USERNAME = "tu-usuario-admin"
PASSWORD = "tu-contraseña-admin"

# Configuración de roles de Redis
ROLES = [
    {
        "name": "db_viewer",
        "management": "db_viewer"
    }, {
        "name": "db_member",
        "management": "db_member"
    }
]

# Configuración de base de datos de Redis
DB_NAME = "database1"
DB_MAX_MEMORY = 1073741824  # 1GB

USERS = [
    {"email": "john.doe@example.com", "name": "John Doe", "role": "db_viewer", "password": "securePass123"},
    {"email": "mike.smith@example.com", "name": "Mike Smith", "role": "db_member", "password": "securePass123"},
    {"email": "cary.johnson@example.com", "name": "Cary Johnson", "role": "admin", "password": "securePass123"}
]
```

## Ejecutar el script
Para ejecutar todas las operaciones automáticamente, ejecuta:

```bash
python redis_api.py
```

También puedes importar la clase `RedisAPI` en otro script y llamar a sus métodos individualmente.

```python
from redis_api import RedisAPI
import config

redis_api = RedisAPI(config.BASE_URL, config.USERNAME, config.PASSWORD)
redis_api.create_database("new_db", 2147483648)  # Crea una base de datos de 2GB
```

## Métodos disponibles
La clase `RedisAPI` proporciona los siguientes métodos:

### `create_role(role)`
Crea un nuevo rol en Redis.
- **Entrada:** Un diccionario con `name`.
- **Ejemplo:**
  ```python
  redis_api.create_role({"name": "db_reader"})
  ```

### `create_database(db_name, max_memory)`
Crea una nueva base de datos en Redis con el nombre y el límite de memoria especificados.
- **Entrada:**
  - `db_name`: Cadena de texto (Nombre de la base de datos)
  - `max_memory`: Entero (Memoria en bytes)
- **Ejemplo:**
  ```python
  redis_api.create_database("my_database", 1073741824)
  ```

### `create_user(user)`
Crea un nuevo usuario con el correo, nombre, rol y contraseña especificados.
- **Entrada:** Un diccionario con `email`, `name`, `role` y `password`.
- **Ejemplo:**
  ```python
  redis_api.create_user({"email": "jane.doe@example.com", "name": "Jane Doe", "role": "db_member", "password": "securePass123"})
  ```

### `list_users()`
Lista todos los usuarios registrados en Redis.
- **Ejemplo:**
  ```python
  redis_api.list_users()
  ```

### `delete_database(db_uid)`
Elimina la base de datos especificada por su ID único.
- **Entrada:**
  - `db_uid`: Entero (UID de la base de datos)
- **Ejemplo:**
  ```python
  redis_api.delete_database(12)
  ```

## Manejo de errores
El script está diseñado para manejar errores de manera eficiente:

- **Errores HTTP:** Detecta fallos de autenticación y solicitudes inválidas.
- **Problemas de conexión:** Maneja fallos de red y caídas del servidor.
- **Parámetros faltantes:** Garantiza que los valores requeridos se proporcionen antes de realizar llamadas a la API.
- **Datos de entrada inválidos:** Evita que se envíen datos incorrectos a la API.

## Salida esperada
Al ejecutarse, el script registra los siguientes mensajes:

- **Mensajes de éxito:**
  ```bash
  Éxito: POST /roles - Código de estado: 200
  Rol 'db_viewer' creado correctamente.
  ```

- **Mensajes de error:**
  ```bash
  Error HTTP: 401 Error de cliente: No autorizado para la URL
  ```

## Solución de problemas
- **Problema: No hay respuesta de la API**
  - Asegúrate de que el servidor de la API está en ejecución y accesible.
  - Verifica `BASE_URL` en `config.py`.

- **Problema: Error de autenticación**
  - Verifica `USERNAME` y `PASSWORD` en `config.py`.
  - Asegúrate de que las credenciales tengan los permisos necesarios para la API.

- **Problema: Los usuarios o roles no aparecen**
  - Comprueba que los roles existen antes de crearlos.
  - Ejecuta `list_users()` para confirmar la creación del usuario.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.