import os
import pytest
import dotenv_switch as ds
from dotenv_switch.exceptions import DotenvSwitchUnspecifiedFilesRequiredError

test_var = 'TEST_VAR'

def test_custom_defaults_none():
    os.environ[ds.default_var] = 'foo'
    ds.load(var=None, fallbacks=None)
    assert os.getenv(test_var) is None

def test_custom_defaults_none_required():
    os.environ[ds.default_var] = 'foo'
    with pytest.raises(DotenvSwitchUnspecifiedFilesRequiredError):
        ds.load(var=None, fallbacks=None, required=True)
