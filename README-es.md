# Prueba de Redis

## Descripción general
En este proyecto, se prueban y validan algunas funciones de Redis Enterprise. Incluye:

**Prueba de replicación de bases de datos**: Un script para probar la replicación de bases de datos de Redis y verificar la sincronización de datos entre la base de datos primaria y la réplica.

**Prueba de API REST**: Un script en Python para automatizar la gestión de bases de datos de Redis a través de su API REST, incluyendo la creación y administración de bases de datos, usuarios y roles.

------------

# TL;DR;

## Cómo conectar y ejecutar pruebas de replicación

### Aviso: Estas instrucciones asumen que tienes una conexión directa con tu clúster de Redis a través de una terminal. Los ejemplos a continuación consideran que estás conectado a un Bastion Host en una VPC privada con un host que ejecuta Alpine Linux y Ubuntu.

1. **Crea tu clúster y bases de datos**  
   El primer paso es crear tu clúster y bases de datos. [Aquí](https://redis.io/docs/latest/operate/rs/databases/create/) hay una documentación que explica este proceso. Para ejecutar la prueba de replicación, necesitas crear dos bases de datos y configurar la replicación. Puedes encontrar instrucciones detalladas [aquí](replication_test/README.md). No olvides anotar los endpoints de las bases de datos, ya que serán necesarios en los siguientes pasos.

2. **Conéctate a tu clúster**  
   Primero, debes obtener acceso a tu clúster. Si estás utilizando una VPC privada, puedes usar un Bastion Host para conectarte e interactuar con tu clúster. La configuración de un Bastion Host está fuera del alcance de este proyecto, pero puedes pedir ayuda si enfrentas problemas.

3. **Instala bibliotecas y otras dependencias**  
   Para asegurarte de que puedes ejecutar estos experimentos, es importante instalar y configurar todas las dependencias y bibliotecas necesarias. Aquí hay una lista de los elementos requeridos:

    - python y pip 3.x  
        - Dependencias de Python: requests, urllib3  
    - redis-cli  
    - git  
    - bash  
    - cmake  
    - make  
    - openssh  

3.1 Ejecuta los siguientes comandos cuando estés conectado a un host con Alpine Linux:

    ```sh
    apk update && apk upgrade 
    apk add --update alpine-sdk
    apk add --no-cache bash git openssh make cmake
    ```

3.2 Descarga y compila `redis-cli`. Puedes compilar las fuentes o instalarlo a través del gestor de paquetes de tu sistema operativo. A continuación, las instrucciones para descargar y compilar:

    ```bash
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make redis-cli
    ```

3.3 Una vez finalizada la compilación, el ejecutable estará en la carpeta `src/`. Usa `redis-cli` para conectarte e interactuar con tus bases de datos.

3.3.1 Crea un registro:

    ```bash
    ./src/redis-cli -u redis://[[SOURCE_DB_ENDPOINT]]
    SET test:tb:1 "test ok"
    ```

3.3.2 Verifica el registro en la base de datos réplica:

    ```bash
    ./src/redis-cli -u redis://[[REPLICA_DB_ENDPOINT]]
    GET test:tb:1
    ```

3.4 Ejecuta el script `replication_test.sh`:

    ```bash
    sh replication_test.sh
    ```

## Cómo conectar y ejecutar pruebas de gestión con la API REST

### Aviso: Estas instrucciones asumen que tienes una conexión directa con tu clúster de Redis a través de una terminal. Los ejemplos a continuación consideran que estás conectado a un Bastion Host en una VPC privada con un host que ejecuta Alpine Linux y Ubuntu.

------------

1. **Antes de ejecutar los scripts**  
   Sigue los mismos pasos 1, 2 y 3 de la sección anterior.

2. **Configuración**  
   Los parámetros y datos utilizados en la prueba de API REST están configurados en el archivo `rest_api_test/config.py`. Hay algunos valores predeterminados, pero puedes cambiarlos según tu escenario. Es importante establecer tu endpoint de API, usuario y contraseña. Puedes encontrar documentación detallada [aquí](https://redis.io/docs/latest/operate/rs/references/rest-api/) y [aquí](replication_test/README.md).

3. **Ejecución**  
   Después de definir los valores en `config.py`, ejecuta:

    ```bash
    python rest_api_test.py
    ```

## Requisitos detallados

1. **Requisitos**  
   - Debes tener una cuenta en Redis Enterprise. Puedes probarlo gratis aquí: [Prueba gratuita](https://redis.io/try-free/). Una vez que tengas acceso, necesitarás credenciales (usuario/contraseña) para interactuar con la API.  
   - Debes tener acceso a una terminal de computadora. Si usas Microsoft Windows, se recomienda [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5).  
   - Conocimientos básicos de programación y uso de una terminal para interactuar con servicios externos.  
   - Para esta prueba, se dispone de un Bastion Host para conectar e interactuar con los servicios de Redis. Pregunta por soporte si necesitas ayuda para conectarte a tu clúster.  

2. **Variables de entorno**  
   Antes de ejecutar los scripts, configura las siguientes variables de entorno en un archivo `.env` o expórtalas en la terminal:

    ```properties
    export REDIS_BASE_URL=[[TU_ENDPOINT]]
    export API_USERNAME=[[TU_USUARIO]]
    export API_PASSWORD=[[TU_CONTRASEÑA]]
    export SOURCE_DATABASE_HOST=[[HOST_BD_PRINCIPAL]]
    export REPLICA_DATABASE_HOST=[[HOST_BD_REPLICA]]
    ```

   Si usas un archivo `.env`, cárgalo en la sesión antes de ejecutar los scripts:

    ```bash
    source .env
    ```

3. **Ejecución interactiva**  
   Puedes realizar estas pruebas ejecutando el script principal (`main.py`) o ejecutando scripts de prueba individuales.

   - Antes de ejecutar, asegúrate de que tienes conectividad con tu clúster. Por ejemplo, los endpoints de VPC privada solo funcionarán si estás conectado a tu clúster.  
   - Para ejecutar el script principal:  

     ```bash
     python main.py
     ```

## Prueba de replicación de bases de datos

El script de prueba de replicación verifica la sincronización de datos entre una base de datos primaria de Redis y su réplica. Esto garantiza que los cambios realizados en la base de datos primaria se reflejen correctamente en la réplica.

Este script fue escrito en bash puro de *nix y utiliza la herramienta `redis-cli`. Para más información sobre el uso de `redis-cli`, consulta la [documentación oficial](https://redis.io/docs/latest/develop/tools/cli/).

### Instrucciones

1. Configura y ejecuta la prueba siguiendo los pasos en [replication_test/README.md](replication_test/README.md).  
2. Asegúrate de que tanto la base de datos primaria como la réplica estén configuradas correctamente.  
3. Verifica que los datos insertados en la base de datos primaria se repliquen en la base de datos réplica.  

## Prueba de API REST

El script de prueba de API automatiza la gestión de bases de datos de Redis a través de una API REST. Ejecuta las siguientes operaciones:  
- Creación y eliminación de bases de datos.  
- Gestión de roles y permisos.  
- Creación, actualización y eliminación de usuarios.  
- Listado de usuarios registrados en Redis.  

### Instrucciones

1. Configura y ejecuta la prueba de API siguiendo los pasos en [api_test/README.md](api_test/README.md).  
2. Asegúrate de que la API esté disponible y accesible.  
3. Verifica que los datos gestionados a través de la API se reflejen correctamente en el sistema Redis. Puedes comprobarlo en el panel principal de Redis Enterprise.  

## Solución de problemas

### La replicación no funciona
- Asegúrate de que las bases de datos primaria y réplica están correctamente configuradas.  
- Usa el comando `redis-cli info replication` para verificar el estado de la replicación.  

### No se puede acceder a la API
- Asegúrate de que la URL de la API (`REDIS_BASE_URL`) en `config.py` es correcta.  
- Verifica que las credenciales (`API_USERNAME`, `API_PASSWORD`) sean válidas.  
- Comprueba que el servidor de la API esté en funcionamiento.  

### Los usuarios o roles no aparecen en Redis
- Asegúrate de que los roles se crean antes de asignarlos a los usuarios.  

## Licencia  
Este proyecto está licenciado bajo la Licencia MIT.