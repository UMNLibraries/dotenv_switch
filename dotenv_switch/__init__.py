from os import getenv
from pathlib import PurePath
from dotenv import load_dotenv, find_dotenv
from dotenv_switch.exceptions import DotenvSwitchFileNotFoundError

# Load the requested dotenv file
# Throw an exception if required but not found
def load(var='APP_ENV', fallbacks=['.env.test', '.env'], required=False, usecwd=False, **kwargs):

    filenames = fallbacks.copy()
    if isinstance(var, str) and getenv(var):
        filenames = [f'.env.{getenv(var)}'] + filenames

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
        raise DotenvSwitchFileNotFoundError(', '.join(filenames_not_found))
    # effectively return an empty dotenv for consistency
    return load_dotenv()
