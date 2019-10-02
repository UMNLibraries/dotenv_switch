import os
import pytest

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_auto_required():

    with pytest.raises(Exception) as exinfo:
        os.environ['APP_ENV'] = 'notexist'
        import dotenv_switch.auto_required

    from dotenv_switch.exceptions import DotenvSwitchFileNotFoundError
    assert exinfo.type == DotenvSwitchFileNotFoundError
