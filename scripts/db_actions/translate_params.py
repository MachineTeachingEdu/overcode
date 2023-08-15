import json

# Read db_params.json
with open("../db_params.json", "r") as db_params_file:
    db_params = json.load(db_params_file)

# Generate .env file
with open(".env.example", "w") as env_file:
    for key, value in db_params.items():
        env_file.write(f"{key.upper()}={value}\n")
