import os
import pathlib
import pytest
import dotenv_switch as ds
from dotenv_switch.exceptions import DotenvSwitchFileNotFoundError
test_var = 'TEST_VAR'

def test_dotenv_missing():
    os.environ[ds.default_var] = 'foo'
    with pytest.raises(DotenvSwitchFileNotFoundError):
        ds.load(required=True)

def test_dotenv_exists(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(required=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]
