import os
import pytest

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_notexist():
    os.environ['APP_ENV'] = 'notexist'

    # TODO: Improve this test to check the specific type of Exception
    # The act of importing the exception from dotenv_switch may mess up the
    # test environment. Fix it later....
    with pytest.raises(Exception):
        import dotenv_switch
