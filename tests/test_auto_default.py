import os

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_auto_default():
    os.environ['APP_ENV'] = ''
    import dotenv_switch.auto
    assert os.getenv('A_VARIABLE') == 'dotenv default test'
