import os

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_foo():
    os.environ['MY_ENV'] = 'foo'
    import dotenv_switch

    dotenv_switch.load('MY_ENV')
    assert os.getenv('A_VARIABLE') == 'dotenv foo'

