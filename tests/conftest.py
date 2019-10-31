import os
import pathlib
import pytest

def remove_dotenv_files():
    for dotenv_file in pathlib.Path.cwd().glob('.env.*'):
        dotenv_file.unlink()
    dotenv = pathlib.Path.cwd() / '.env'
    if dotenv.exists():
        dotenv.unlink()

def remove_env_vars():
    for env_var in ('APP_ENV', 'MY_ENV', 'TEST_VAR'):
        if env_var in os.environ:
            os.environ.pop(env_var)

def pytest_runtest_setup(item):
    remove_dotenv_files()
    remove_env_vars()

def pytest_runtest_teardown(item):
    remove_dotenv_files()
    remove_env_vars()

@pytest.fixture()
def create_dotenv_files():
    def _create_dotenv_files(path, dotenv_file_metadata={}):
        dotenv_files = []
        for dotenv_filename, env_vars in dotenv_file_metadata.items():
            dotenv_file = path / dotenv_filename 
            for k, v in env_vars.items():
                dotenv_file.write_text(f'{k}="{v}"\n')
            dotenv_files.append(dotenv_file)
        return dotenv_files
    return _create_dotenv_files
