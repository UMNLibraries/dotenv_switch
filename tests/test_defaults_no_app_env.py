import os
import dotenv_switch as ds
test_var = 'TEST_VAR'

def test_no_dotenv_files():
    ds.load()
    assert os.getenv(test_var) is None

def test_dotenv_only(create_dotenv_files):
    dotenv_file_metadata = {
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(dotenv_file_metadata)
    ds.load()
    assert os.getenv(test_var) == dotenv_file_metadata['.env'][test_var]

def test_all_fallbacks(create_dotenv_files):
    dotenv_file_metadata = {
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(dotenv_file_metadata)
    ds.load(override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]

def test_all_fallbacks_and_dotenv_foo(create_dotenv_files):
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(dotenv_file_metadata)
    ds.load(override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]

def test_dotenv_foo_only(create_dotenv_files):
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(dotenv_file_metadata)
    ds.load(override=True)
    assert os.getenv(test_var) is None
