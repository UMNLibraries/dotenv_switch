import os
import pathlib

test_var = 'TEST_VAR'
for env_var in ('APP_ENV', test_var):
    if env_var in os.environ:
        os.environ.pop(env_var)
os.environ['APP_ENV'] = 'foo'

def test_no_dotenv_files():
    import dotenv_switch.auto
    assert os.getenv(test_var) == None

def test_dotenv_only(create_dotenv_files, delete_dotenv_files):
    if test_var in os.environ:
        os.environ.pop(test_var)
    dotenv_file_metadata = {
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    import dotenv_switch.auto
    assert os.getenv(test_var) == dotenv_file_metadata['.env'][test_var]
    delete_dotenv_files(dotenv_files)

def test_all_fallbacks(create_dotenv_files, delete_dotenv_files):
    if test_var in os.environ:
        os.environ.pop(test_var)
    dotenv_file_metadata = {
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    import dotenv_switch.auto
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]
    delete_dotenv_files(dotenv_files)

def test_all_fallbacks_and_dotenv_foo(create_dotenv_files, delete_dotenv_files):
    if test_var in os.environ:
        os.environ.pop(test_var)
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    import dotenv_switch.auto
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]
    delete_dotenv_files(dotenv_files)

def test_dotenv_foo_only(create_dotenv_files, delete_dotenv_files):
    if test_var in os.environ:
        os.environ.pop(test_var)
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    import dotenv_switch.auto
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]
    delete_dotenv_files(dotenv_files)
