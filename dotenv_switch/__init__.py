from os import getenv
from pathlib import PurePath
from dotenv import load_dotenv, find_dotenv
from dotenv_switch.exceptions import DotenvSwitchUnspecifiedFilesRequiredError, DotenvSwitchFileNotFoundError

default_var = 'APP_ENV'
default_fallbacks = ['.env.test', '.env']
default_required = False
default_usecwd = False

# Load the requested dotenv file
# Throw an exception if required but not found
def load(var=default_var, fallbacks=default_fallbacks, required=default_required, usecwd=default_usecwd, **kwargs):

    filenames = fallbacks.copy() if isinstance(fallbacks, list) else []
    if isinstance(var, str) and getenv(var):
        filenames = [f'.env.{getenv(var)}'] + filenames

    if required and len(filenames) == 0:
        raise DotenvSwitchUnspecifiedFilesRequiredError

    filenames_not_found = []
    for filename in filenames:
        try:
            return load_dotenv(
                find_dotenv(
                    filename=filename,
                    raise_error_if_not_found=True,
                    usecwd=usecwd
                ),
                **kwargs
            )
        except IOError:
            filenames_not_found.append(filename)
            pass

    if required:
        raise DotenvSwitchFileNotFoundError(filenames_not_found)
    # effectively return an empty dotenv for consistency
    return load_dotenv()
