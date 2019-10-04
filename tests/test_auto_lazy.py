import os

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_auto_lazy():
    os.environ['APP_ENV'] = 'fallbackplease'
    import dotenv_switch.auto_lazy
    assert os.getenv('A_VARIABLE') == 'dotenv lazy fallback'

