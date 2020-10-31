#! /Users/tarou/0_project/auto_translate/0_env/bin/python

import os
from os.path import join, dirname
from dotenv import load_dotenv


load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_URL = os.environ.get("GOOGLE_API")