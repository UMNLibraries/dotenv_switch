import os

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_foo():
    os.environ['APP_ENV'] = 'foo'
    import dotenv_switch
    assert os.getenv('A_VARIABLE') == 'dotenv foo'

