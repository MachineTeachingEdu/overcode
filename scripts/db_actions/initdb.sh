#!/bin/bash
set -e

# Wait for the PostgreSQL container to be up and running
until PGPASSWORD=$PASSWORD psql -h "$HOST" -U "$USER" -d "$DATABASE" -c '\l' > /dev/null 2>&1; do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 1
done

# Restore the database from the backup
PGPASSWORD=$PASSWORD pg_restore -h "$HOST" -U "$USER" -d "$DATABASE" -Fc /docker-entrypoint-initdb.d/db_dump.backup
