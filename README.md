
# postgres-supabase-iac

A simple infrastructure-as-code setup for running Postgres with Supabase using Docker.

## Getting Started

1. **Rename the Project**

    Update the project name in all relevant files and directories from `postgres_subapase_iac` to your preferred name.

2. **Start the Docker Containers**

    ```bash
    docker compose up -d
    ```

3. **Install Python Dependencies**

    ```bash
    poetry install
    ```

    This will install all required components and enable the `postgres-supabase` command.

## Notes

- To stop and remove all Docker containers and associated volumes:

  ```bash
  docker compose down -v
  ```

