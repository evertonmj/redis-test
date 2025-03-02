# Script de Prueba de Replicación en Redis

## Descripción General

Este script en Bash está diseñado para probar la replicación en Redis insertando valores en una base de datos de origen y luego recuperándolos desde una base de datos réplica.

## Requisitos Previos

Asegúrate de tener Redis instalado y en ejecución. También necesitarás:

- Una cuenta en Redis Enterprise creada.
- Bases de datos de origen y réplica configuradas.
- Acceso a tu clúster directamente o a través de un bastion host. Puedes consultar cómo interactuar con tus recursos de Redis en este [enlace](https://redis.io).
- `redis-cli` instalado. Para instalar `redis-cli` en tu sistema, consulta la [guía de instalación](https://redis.io/topics/rediscli).
- Variables de entorno configuradas para los endpoints de las bases de datos de origen y réplica.

## Configuración

Sigue estos pasos para crear y configurar las bases de datos de origen y réplica:

1. Crea una base de datos Redis Enterprise con un solo shard llamada `source-db`, sin contraseña y con un límite de memoria de 2GB. Puedes aprender cómo crear bases de datos Redis Enterprise [aquí](https://redis.io/topics/redisenterprise).

2. Habilita la opción "Replica Of" creando otra base de datos Redis Enterprise con un solo shard llamada `replica-db`, sin contraseña y con un límite de memoria de 2GB. Usa `source-db` como la base de datos de origen.

3. Después de crear las bases de datos, obtén los endpoints de `source-db` y `replica-db` y configura las siguientes variables de entorno antes de ejecutar el script:

    ```sh
    export SOURCE_DATABASE_HOST="tu-host-redis-origen"
    export REPLICA_DATABASE_HOST="tu-host-redis-replica"
    ```

    Alternativamente, puedes crear un archivo `.env` y cargarlo con:

    ```sh
    source .env
    ```

4. Conéctate a tu clúster y ejecuta el script.

## Cómo Funciona

El script inserta los números del 1 al 100 en una lista de Redis en la base de datos de origen.

Luego, extrae estos números desde la base de datos réplica para verificar la replicación. El tipo de datos List en Redis mantiene un orden natural, por lo que no es necesario preocuparse por ordenar los elementos manualmente.

Redis proporciona los comandos `RPUSH`, `LPUSH`, `RPOP` y `LPOP`. El script usa `RPUSH` para insertar los elementos al final de la lista. Para recuperarlos en orden inverso, usa `RPOP` para extraer el último elemento y mostrarlo en pantalla. De esta manera, no es necesario preocuparse por el orden de los elementos.

## Ejecución del Script

Ejecuta el script con los siguientes comandos:

```sh
chmod +x replication_test.sh
./replication_test.sh
```

## Salida Esperada

- Confirmación de que los números se han agregado correctamente a la base de datos de origen imprimiéndolos en la consola.
- Confirmación de que los números se han recuperado desde la base de datos réplica imprimiéndolos en orden inverso.

## Solución de Problemas

- Si la replicación no funciona, asegúrate de que las bases de datos de origen y réplica estén correctamente configuradas.
- Verifica si las variables de entorno están configuradas correctamente con los endpoints de `source-db` y `replica-db`.
- Asegúrate de que la replicación está habilitada y de que `source-db` está correctamente configurada como la fuente en `replica-db`.
- Revisa los logs de Redis para confirmar que la replicación está activa.

## Mejoras Futuras

- Crear automáticamente las bases de datos de origen y réplica usando `redis-cli`.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.