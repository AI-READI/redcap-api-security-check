#!/usr/bin/env python

from dotenv import dotenv_values
from os import environ
from pathlib import Path
from redcap import Project
from sys import exit

# Check if `.env` file exists
env_path = Path(".") / ".env"

LOCAL_ENV_FILE = env_path.exists()

config = dotenv_values(".env")

def get_env(key):
    """Return environment variable from .env or native environment."""
    if LOCAL_ENV_FILE:
        return config.get(key)

    if key not in environ:
        raise ValueError(f"Environment variable {key} not set.")

    return environ.get(key)

token = get_env('REDCAP_TOKEN')
url = get_env('REDCAP_URL')

prj = Project(url, token)
df = prj.export_metadata(format_type='df')

phi_fields = df[df["identifier"] == "y"]

data_df = prj.export_records(fields = phi_fields.index.to_list(), format_type = "df")

assert len(data_df.columns.to_list()) == 2, "REDCap returned invalid number of columns"
