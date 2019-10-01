import sys
from os import getenv
from dotenv import load_dotenv, find_dotenv
from dotenv_switch.exceptions import *

# Read $APP_ENV, default to 'test' for filename like .env.test
app_env_file = '.env.' + (getenv('APP_ENV') or 'test').lower()

try:
    # Load the requested dotenv file
    load_dotenv(find_dotenv(filename=app_env_file, raise_error_if_not_found=True, usecwd=True))
except IOError:
    raise DotenvSwitchFileNotFoundError(app_env_file)
