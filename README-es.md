# Redis Test

## Descripción General
Este proyecto proporciona herramientas y scripts para gestionar y probar bases de datos Redis. Incluye:

1. **Prueba de Replicación**: Un script para probar la replicación de Redis y verificar la sincronización de datos entre bases de datos primarias y réplicas.
2. **Prueba de API**: Un script en Python para automatizar la gestión de bases de datos Redis mediante una API REST, incluyendo la creación de bases de datos, usuarios y roles.

## Prueba de Replicación

El script de prueba de replicación verifica la sincronización de datos entre una base de datos Redis primaria y su réplica. Esto garantiza que los cambios realizados en la base de datos primaria se reflejen correctamente en la réplica.

### Instrucciones

1. Configura y ejecuta la prueba siguiendo los pasos en [replication_test/README.md](replication_test/README.md).
2. Asegúrate de que tanto la base de datos primaria como la réplica estén configuradas correctamente.
3. Verifica que los datos insertados en la base de datos primaria se repliquen en la base de datos réplica.

## Prueba de API

El script de prueba de API automatiza el proceso de gestión de bases de datos Redis mediante una API REST. Permite realizar operaciones como:
- Crear y eliminar bases de datos.
- Gestionar roles y permisos.
- Crear, actualizar y eliminar usuarios.
- Listar usuarios registrados en Redis.

### Instrucciones

1. Configura y ejecuta la prueba de API siguiendo los pasos en [api_test/README.md](api_test/README.md).
2. Asegúrate de que la API esté disponible y accesible.
3. Verifica que los datos administrados a través de la API se reflejen correctamente en el sistema Redis.

## Requisitos Previos
Para ejecutar correctamente los scripts de prueba, asegúrate de cumplir con los siguientes requisitos:

- Redis Enterprise instalado y configurado correctamente.
- Python 3.x instalado en tu sistema.
- Instalación de las dependencias necesarias:

```bash
pip install requests urllib3
```

## Variables de Entorno
Antes de ejecutar los scripts, configura las siguientes variables de entorno en un archivo `.env` o expórtalas en la terminal:

```properties
export REDIS_BASE_URL=[[TU_ENDPOINT]]
export API_USERNAME=[[TU_USUARIO]]
export API_PASSWORD=[[TU_CONTRASEÑA]]
export SOURCE_DATABASE_HOST=[[HOST_BD_ORIGEN]]
export REPLICA_DATABASE_HOST=[[HOST_BD_RÉPLICA]]
```

Si utilizas un archivo `.env`, cárgalo en la sesión antes de ejecutar los scripts:

```bash
source .env
```

## Solución de Problemas
### 1. La replicación no funciona
- Asegúrate de que la base de datos primaria y la réplica estén configuradas correctamente.
- Usa el comando `redis-cli info replication` para verificar el estado de la replicación.

### 2. No se puede acceder a la API
- Asegúrate de que la URL de la API (`REDIS_BASE_URL`) en `config.py` sea correcta.
- Verifica que las credenciales (`API_USERNAME`, `API_PASSWORD`) sean válidas.
- Confirma que el servidor de la API esté en ejecución.

### 3. Los usuarios o roles no aparecen en Redis
- Asegúrate de que los roles se creen antes de asignarlos a los usuarios.
- Usa la función `list_users()` en el script de prueba de API para verificar los usuarios registrados.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.

