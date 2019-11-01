import os
import pathlib
import pytest

def remove_dotenv_files():
    '''Removes test dotenv files from the current working directory.

    This function is for cleaning up between tests. Note the potentially
    dangerous assumptions that any and all test dotenv filenames will
    be either `.env` or match the glob pattern `.env.*`, and will exist
    only in the current working directory. Violating these assumptions
    may cause test failures.
    '''
    for dotenv_file in pathlib.Path.cwd().glob('.env.*'):
        dotenv_file.unlink()
    generic_dotenv = pathlib.Path.cwd() / '.env'
    if generic_dotenv.exists():
        generic_dotenv.unlink()

def remove_env_vars():
    '''Removes test env vars from the current working directory

    This function is for cleaning up between tests. Note the potentially
    dangerous assumption that tests will never create environment
    variables named anything other than `APP_ENV`, `MY_ENV`, or
    `TEST_VAR`. If that assumption is no longer true, this function
    must be updated accordingly. Failure to do so may cause test
    failures.
    '''
    for env_var in ('APP_ENV', 'MY_ENV', 'TEST_VAR'):
        if env_var in os.environ:
            os.environ.pop(env_var)

def pytest_runtest_setup(item):
    '''Pre-test cleanup of dotenv files and env vars

    We do this before each test invocation in case a previous test
    failed to clean up after itself.
    '''
    remove_dotenv_files()
    remove_env_vars()

def pytest_runtest_teardown(item):
    '''Post-test cleanup of dotenv files and env vars

    We do this here rather than in test functions because, if an
    assertion fails, any code following that assertion will not be
    executed.
    '''
    remove_dotenv_files()
    remove_env_vars()

@pytest.fixture()
def create_dotenv_files():
    '''pytest fixture returning function that creates dotenv files in the current working directory

    Parameters
    ----------
    dotenv_file_metadata : dict
        map of dotenv file basenames to dicts of their key-value pairs

    Returns
    -------
    function
         function that creates dotenv files in the current working directory
    '''
    def _create_dotenv_files(dotenv_file_metadata={}):
        dotenv_files = []
        for dotenv_filename, env_vars in dotenv_file_metadata.items():
            dotenv_file = pathlib.Path.cwd() / dotenv_filename 
            for k, v in env_vars.items():
                dotenv_file.write_text(f'{k}="{v}"\n')
            dotenv_files.append(dotenv_file)
        return dotenv_files
    return _create_dotenv_files
