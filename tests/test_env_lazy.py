import os

# Empty value for APP_ENV
os.chdir(os.path.dirname(os.path.realpath(__file__)))

def test_dotenv_lazy_fallback():
    os.environ['APP_ENV'] = 'fallbackplease'
    import dotenv_switch

    dotenv_switch.load(lazy=True)
    assert os.getenv('A_VARIABLE') == 'dotenv lazy fallback'
