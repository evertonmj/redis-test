# Redis Test

## Overview
In this project, some Redis Enterprise features are tested and validated. It includes:

**Databases Replication Test**: A script to test Redis database replication and verify data synchronization between primary and replica databases.

**REST API Test**: A Python script to automate Redis database management via its REST API, including creating and managing databases, users, and roles.

------------

# TL;DR;

## How to connect and run replication tests

#### Disclaimer: These instructions assume that you have a direct connection with your Redis Cluster via a terminal. The examples below consider that you are connected to a Bastion Host in a private VPC with a host running Alpine Linux

1. **Create your cluster and databases**
   The first step is to create your cluster and your databases. [Here](https://redis.io/docs/latest/operate/rs/databases/create/) there is a doc explaining this process. To run the Replication Test, you need to create two databases and configure replication. You can find detailed instructions [here](replication_test/README.md). Don't forget to take note of database endpoints. They will be necessary in the next steps.

2. **Connect to your cluster**
   The first step is to gain access to your cluster. If you are using a private VPC, you can use a bastion host to connect and interact with your cluster. Provisioning and configuring a Bastion Host is outside the scope of this project, but feel free to ask for help if you are facing problems.

3. **Install libraries and other dependencies**
   To ensure that you will be able to run these experiments, it's important to install and configure all required dependencies and libraries. Here is a list of required items:

    - python and pip 3.x
        - python dependencies: requests, urllib3
    - redis-cli
    - git
    - bash
    - cmake
    - make
    - openssh

3.1 Run the following commands when connected to an Alpine Linux host:

    ```sh
    apk update && apk upgrade 
    apk add --update alpine-sdk
    apk add --no-cache bash git openssh make cmake
    ```

3.2 Download and compile redis-cli. You can compile the sources or install via your Operating System package manager. Below are the instructions to download and compile:

    ```bash
    wget http://download.redis.io/redis-stable.tar.gz
    tar xvzf redis-stable.tar.gz
    cd redis-stable
    make redis-cli
    ```

3.3 When the compile is finished, the executable will be in the `src/` folder. Use redis-cli to connect and interact with your databases.

3.3.1 Connect to source-db and create a record:

    ```bash
    ./src/redis-cli -u redis://[[SOURCE_DB_ENDPOINT]]
    SET test:tb:1 "test ok"
    ```

3.3.2 Connecto to replica-db and check the replica database for the record:

    ```bash
    ./src/redis-cli -u redis://[[REPLICA_DB_ENDPOINT]]
    GET test:tb:1
    ```

3.4 Run the `replication_test.sh` script:

    ```bash
    sh replication_test.sh
    ```

## How to connect and run REST API management tests

### Disclaimer: These instructions assume that you have a direct connection with your Redis Cluster via a terminal. The examples below consider that you are connected to a Bastion Host in a private VPC with a host running Alpine Linux and Ubuntu.

------------

1. **Before Running the Scripts**
   Follow the same steps 1, 2, and 3 from the previous section.

2. **Configuration**
   The parameters and data used in the REST API experiment are configured in the `rest_api_test/config.py` file. There are some default parameters, but you can change them to your own scenario. It's important to set your API endpoint, user, and password. Detailed documentation can be found [here](https://redis.io/docs/latest/operate/rs/references/rest-api/) and [here](replication_test/README.md).

3. **Running**
   After setting values in the `config.py` file, just run:

    ```bash
    python rest_api_test.py
    ```

## Detailed Requirements

1. **Requirements**
   - You must have a Redis Enterprise Account. You can try it for free here: [Try it for free](https://redis.io/try-free/). After getting access to your account, you will need credentials (user/password) to interact with the API.
   - You must have access to a computer terminal. If you are using Microsoft Windows, [Powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5) is highly recommended.
   - Basic programming skills and knowledge of how to use a computer terminal to interact with external services.
   - For the purposes of this test, a Bastion Host was available to connect and interact with Redis Services. Please, ask for support about how you can get ready to connect and interact with your cluster.

2. **Environment Variables**
   Before running the scripts, set up the following environment variables in a `.env` file or export them in the terminal:

    ```properties
    export REDIS_BASE_URL=[[YOUR_ENDPOINT]]
    export API_USERNAME=[[YOUR_USER]]
    export API_PASSWORD=[[YOUR_PASSWORD]]
    export SOURCE_DATABASE_HOST=[[SOURCE_DB_HOST]]
    export REPLICA_DATABASE_HOST=[[REPLICA_DB_HOST]]
    ```

   If using a `.env` file, load it into the session before executing the scripts:

    ```bash
    source .env
    ```

3. **Running Interactively**
   You can perform these tests by running the main python script (`main.py`) or by running individual test scripts.

   - Before running, it's important to ensure that you have connectivity to your cluster. For example, private VPC endpoints will work only if you are connected to your cluster.
   - To run the main script: `python main.py`

## Database Replication Test

The replication test script verifies data synchronization between a primary Redis database and its replica. This ensures that changes made in the primary database are correctly reflected in the replica.

This script was written in pure *nix bash and redis-cli tool. For more information on using the Redis CLI, refer to the [official documentation](https://redis.io/docs/latest/develop/tools/cli/).

### Instructions

1. Set up and run the test by following the steps in [replication_test/README.md](replication_test/README.md).
2. Ensure both the primary and replica databases are properly configured.
3. Verify that data inserted into the primary database is replicated to the replica database.

## REST API Test

The API test script automates the process of managing Redis databases via a REST API. It executes the following operations:
- Creating and deleting databases.
- Managing roles and permissions.
- Creating, updating, and deleting users.
- Listing registered users in Redis.

### Instructions

1. Set up and run the API test by following the steps in [api_test/README.md](api_test/README.md).
2. Ensure the API is available and accessible.
3. Verify that data managed through the API is correctly reflected in the Redis system. You can check it at the Redis Enterprise main dashboard.

## Troubleshooting

### Replication is not working
- Ensure the primary and replica databases are correctly configured.
- Use the command `redis-cli info replication` to check replication status.

### Unable to access the API
- Ensure the API URL (`REDIS_BASE_URL`) in `config.py` is correct.
- Verify that the credentials (`API_USERNAME`, `API_PASSWORD`) are valid.
- Check that the API server is running.

### Users or roles do not appear in Redis
- Ensure that roles are created before assigning them to users.

## License
This project is licensed under the MIT License.

