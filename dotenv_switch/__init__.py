import sys
from os import getenv
from dotenv import load_dotenv, find_dotenv
from dotenv_switch.exceptions import DotenvSwitchFileNotFoundError

# Read $APP_ENV, default to 'test' for filename like .env.test
def env_file(var='APP_ENV'):
    return '.env.' + (getenv(var) or 'test').lower()

# Load the requested dotenv file
# Throw an exception if required but not found
def load(var='APP_ENV', required=False):
    try:
        load_dotenv(find_dotenv(filename=env_file(var), raise_error_if_not_found=required, usecwd=True))
    except IOError:
        raise DotenvSwitchFileNotFoundError(env_file())
