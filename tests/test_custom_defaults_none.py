import os
import pathlib
import pytest
import dotenv_switch as ds
from dotenv_switch.exceptions import DotenvSwitchUnspecifiedFilesRequiredError

test_var = 'TEST_VAR'
for env_var in (ds.default_var, test_var):
    if env_var in os.environ:
        os.environ.pop(env_var)
os.environ[ds.default_var] = 'foo'

def test_custom_defaults_none():
    ds.load(var=None, fallbacks=None)
    assert os.getenv(test_var) is None

def test_custom_defaults_none_required():
    with pytest.raises(DotenvSwitchUnspecifiedFilesRequiredError):
        ds.load(var=None, fallbacks=None, required=True)
