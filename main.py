#!/usr/bin/env python

import os
import sys

from dotenv import load_dotenv
from redcap import Project

load_dotenv()
token = os.getenv('REDCAP_TOKEN')
url = os.getenv('REDCAP_URL')

prj = Project(url, token)
df = prj.export_metadata(format_type='df')

phi_fields = df[df["identifier"] == "y"]

data_df = prj.export_records(fields = phi_fields.index.to_list(), format_type = "df")

if len(data_df.columns.to_list()) > 2:
    sys.exit(1)
