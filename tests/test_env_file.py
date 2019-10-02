import os
import dotenv_switch

def test_env_file_default():
    assert dotenv_switch.env_file() == '.env.test'

def test_env_file_alternate_default():
    assert dotenv_switch.env_file(default_env='alt') == '.env.alt'

def test_env_file_default_env_var():
    os.environ['APP_ENV'] = 'myenv'
    assert dotenv_switch.env_file() == '.env.myenv'

def test_env_file_alternate_env_var():
    os.environ['MY_ENV'] = 'myenv'
    assert dotenv_switch.env_file(var='MY_ENV') == '.env.myenv'

def test_env_file_alternate_env_var_empty():
    os.environ['MY_ENV'] = ''
    assert dotenv_switch.env_file(var='MY_ENV') == '.env.test'
    assert dotenv_switch.env_file(var='MY_ENV', default_env='alt') == '.env.alt'
