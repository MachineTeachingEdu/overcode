#!/bin/sh
set -e  # Interrupt on error

# Build the images and start the containers
docker compose up --detach --build

# Run the CLI application and wait for its completion
docker exec -it overcode-container /bin/bash -c "cd /app && python master_script.py 745"

# After the CLI application exits, stop and remove the containers
docker-compose down
