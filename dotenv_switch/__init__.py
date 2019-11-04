from os import getenv
from pathlib import PurePath
from dotenv import load_dotenv, find_dotenv
from dotenv_switch.exceptions import DotenvSwitchUnspecifiedFilesRequiredError, DotenvSwitchFileNotFoundError

default_var = 'APP_ENV'
default_fallbacks = ['.env.test', '.env']
default_required = False
default_usecwd = False

def load(var=default_var, fallbacks=default_fallbacks, required=default_required, usecwd=default_usecwd, **kwargs):
    '''Loads a dotenv file based on an env var and a list of fallback filenames

    Parameters
    ----------
    var : str, optional
        name of the env var specifying the desired environemnt
        (default is APP_ENV)
    fallbacks : list, optional
        list of dotenv filenames to use if var is None or .env.{var} is
        not found (default is ['.env.test','.env'])
    required : bool, optional
        whether to raise an exception if no dotenv file is found
        (default is False)
    usecwd : bool, optional
        dotenv.find_dotenv() param, with the same default, which will be
        passed to that function (default is False)
    **kwargs : optional
        any remaining params will be passed to dotenv.load_dotenv()
        
    Raises
    ------
    DotenvSwitchUnspecifiedFilesRequiredError
        If required is True, but var is None or .env.{var} cannot be
        found, and fallbacks is None or empty.
    DotenvSwitchFileNotFoundError
        If required is True but no dotenv file can be found.

    Returns
    -------
    DotEnv
       the object returned by dotenv.loadenv()
    '''

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
    return load_dotenv(**kwargs)
