import os
import tomllib

env = os.getenv("APP_ENV", "dev")
config_path = f"config/{env}.toml"

if not os.path.exists(config_path):
    raise RuntimeError(f"config file not found for environment: {env}")

with open(config_path, "rb") as f:
    config = tomllib.load(f)
