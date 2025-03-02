# Redis Project

This project contains scripts and tools for managing and testing Redis databases. It includes:

1. **Replication Test**: A script to test Redis replication.
2. **API Test**: A Python script to automate Redis database management via API.

## Replication Test

The replication test script helps you set up and verify Redis replication between two databases.

### Instructions

1. Follow the steps in the [replication_test/README.md](replication_test/README.md) to set up and run the replication test.

## API Test

The API test script automates the process of managing Redis databases, including creating roles, databases, and users.

### Instructions

1. Follow the steps in the [api_test/README.md](api_test/README.md) to configure and run the API test script.

## Prerequisites

- Redis Enterprise installed and configured
- Python 3.x installed
- Required Python packages: `requests`, `urllib3`

## Environment Variables

Set up the following environment variables in a `.env` file or export them in your shell:

```properties
export REDIS_BASE_URL=[[YOUR_ENDPOINT]]
export API_USERNAME=[[YOUR_USER]]
export API_PASSWORD=[[YOUR_PASS]]
export SOURCE_DATABASE_HOST=[[SOURCE_DB]]
export REPLICA_DATABASE_HOST=[[REPLICA_DB]]

```

## License

This project is licensed under the MIT License.
