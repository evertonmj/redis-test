# Redis Replication Test

This guide will help you set up a Redis replication test using Redis Enterprise databases.

## Prerequisites

- Redis Enterprise installed and configured
- Access to a load node

## Instructions

### 1. Create Source Database

Create a single-sharded Redis Enterprise database named `source-db` with no password and a memory limit of 2GB. You can learn how to create Redis Enterprise databases [here](https://docs.redislabs.com/latest/rs/administering/creating-databases/).

### 2. Enable Replica Of

Create another single-sharded Redis Enterprise database named `replica-db` with no password and a memory limit of 2GB. Use `source-db` as the source database.

### 3. Connect on the bastion host using the link on doc page

### 4. Install and configure tools:

#### 4.1 Update package manager
```sh
apk update && apk upgrade 
apk add --update alpine-sdk
```

#### 4.2 Install git, bash and compiling tools
```sh
apk add --no-cache bash git openssh make cmake
```

#### 4.3 Get redis source code
```sh
wget http://download.redis.io/redis-stable.tar.gz
```

#### 4.4 Unpack and compile redis
```sh
tar xvzf redis-stable.tar.gz
cd redis-stable
make redis-cli
```

#### 4.5 Copy Redis executable
```sh
sudo cp src/redis-cli ~
```

#### 4.6 Connect to source database and insert value

##### 4.6.1 Connect to source db node: 
```sh
./src/redis-cli -u redis://<SOURCE_DB_ENDPOINT>>:<SOURCE_DB_PORT>
```

##### 4.6.2 Insert value
```sh
SET test:tb:1 "test ok"
```

#### 4.7 Connect to replica database and check if value is inserted

##### 4.7.1 Connect to replica db node: 
```sh
./src/redis-cli -u redis://<REPLICA_DB_ENDPOINT>>:<REPLICA_DB_PORT>
```

##### 4.7.2 Check if value is inserted
```sh
GET test:tb:1
```

### 5. Run test case ###

#### 5.1 Download test script
```sh
wget https://raw.githubusercontent.com/evertonmj/redis-test/refs/heads/main/replication-test.sh
```

#### 5.2 Update databases endpoints

##### 5.2.1 Open the replication-test.sh file
```sh
vim replication-test.sh
```

##### 5.2.2 Update endpoints

Update endpoints for SOURCE_DB and REPLICA_DB with recent created databases and close the file.

Press esc key and them `:wq` to save and exit.

#### 5.2 Execute
```sh
sh replication-test.sh
```
