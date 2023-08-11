import json
import subprocess

# Load database parameters from db_params.json
with open("../db_params.json", "r") as f:
    db_params = json.load(f)

# Extract parameters
host = db_params["host"]
port = "5432"
user = db_params["user"]
password = db_params["password"]
dbname = db_params["database"]
dump_file = "db_dump.backup" 

# Restore data from the dump file to the target database
restore_command = [
    "pg_restore",
    dump_file,
    "--clean",
    "--dbname", dbname,
    "--host", host,
    "--port", port,
    "--username", user,
    "--no-password",
    "--verbose",
]
subprocess.run(restore_command)
