#!/bin/sh
set -e  # Interrupt on error

# Build the images and start the containers
docker compose up -d

# Run the master script inside the application container
docker compose exec app python master_script.py

# Stop and remove the containers
docker compose down

