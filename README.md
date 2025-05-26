
# postgres-supabase-iac

A straightforward infrastructure-as-code setup for running PostgreSQL with Supabase using Docker.

## Getting Started

1. **Rename the Project**

    Replace all instances of `postgres_subapase_iac` in files and directories with your desired project name.

2. **Configure Environment Variables**

    - Copy `.env.sample` to `.env`.
    - Update the connection URI and other settings in `.env` as needed.

3. **Start Docker Containers**

    ```bash
    docker compose up -d
    ```

4. **Install Python Dependencies**

    ```bash
    poetry install
    ```

    This will install all required dependencies and make the `postgres-supabase` command available.

5. **Create Database Tables**

    Run the following command (as defined in your `pyproject.toml`):

    ```bash
    postgres-supabase create-tables
    ```

## Notes

- To stop and remove all Docker containers and associated volumes, run:

    ```bash
    docker compose down -v
    ```
