import os
import pathlib
import pytest
import dotenv_switch as ds
from dotenv_switch.exceptions import DotenvSwitchFileNotFoundError
test_var = 'TEST_VAR'

for env_var in (ds.default_var, test_var):
    if env_var in os.environ:
        os.environ.pop(env_var)
os.environ[ds.default_var] = 'foo'

def test_dotenv_missing():
    with pytest.raises(DotenvSwitchFileNotFoundError):
        ds.load(required=True)

def test_dotenv_exists(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(required=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]
    delete_dotenv_files(dotenv_files)
