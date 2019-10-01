import sys
from os import getenv
from dotenv import load_dotenv, find_dotenv

# Read $APP_ENV, default to 'test' for filename like .env.test
app_env_file = '.env.' + (getenv('APP_ENV') or 'test').lower()

# Load the requested dotenv file
load_dotenv(find_dotenv(filename=app_env_file, raise_error_if_not_found=True, usecwd=True))
