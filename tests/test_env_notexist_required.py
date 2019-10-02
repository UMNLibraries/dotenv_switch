import os, sys, pytest

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_notexist():
    os.environ['APP_ENV'] = 'notexist'
    import dotenv_switch

    # Variable should be unset but test passes, no exception thrown
    dotenv_switch.load()
    assert os.getenv('A_VARIABLE') is None

