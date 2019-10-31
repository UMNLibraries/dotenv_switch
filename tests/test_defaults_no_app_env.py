import os
import pathlib
import dotenv_switch as ds
test_var = 'TEST_VAR'

for env_var in (ds.default_var, test_var):
    if env_var in os.environ:
        os.environ.pop(env_var)

def test_no_dotenv_files():
    ds.load()
    assert os.getenv(test_var) == None

def test_dotenv_only(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load()
    assert os.getenv(test_var) == dotenv_file_metadata['.env'][test_var]
    delete_dotenv_files(dotenv_files)

def test_all_fallbacks(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]
    delete_dotenv_files(dotenv_files)

def test_all_fallbacks_and_dotenv_foo(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]
    delete_dotenv_files(dotenv_files)

def test_dotenv_foo_only(create_dotenv_files, delete_dotenv_files):
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(override=True)
    assert os.getenv(test_var) == None
    delete_dotenv_files(dotenv_files)
