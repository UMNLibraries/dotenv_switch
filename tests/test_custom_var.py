import os
import pathlib
import dotenv_switch as ds
custom_var = 'MY_ENV'
test_var = 'TEST_VAR'

for env_var in (custom_var, test_var):
    if env_var in os.environ:
        os.environ.pop(env_var)
os.environ[custom_var] = 'foo'

def test_custom_var(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(var=custom_var)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]
    delete_dotenv_files(dotenv_files)

def test_custom_var_is_none(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env.test': {test_var: 'dotenv test'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(var=None)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]
    delete_dotenv_files(dotenv_files)

