import os
import pathlib
import dotenv_switch as ds

test_var = 'TEST_VAR'
fallbacks = ['.env.dev','.env.stg','.env.prd']

def test_no_dotenv_files():
    os.environ[ds.default_var] = 'foo'
    ds.load()
    assert os.getenv(test_var) is None

def test_no_dotenv_dev(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.stg': {test_var: 'dotenv stg'},
        '.env.prd': {test_var: 'dotenv prd'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(fallbacks=fallbacks)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.stg'][test_var]

def test_all_fallbacks(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.dev': {test_var: 'dotenv dev'},
        '.env.stg': {test_var: 'dotenv stg'},
        '.env.prd': {test_var: 'dotenv prd'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(fallbacks=fallbacks, override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.dev'][test_var]

def test_all_fallbacks_and_dotenv_foo(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
        '.env.dev': {test_var: 'dotenv dev'},
        '.env.stg': {test_var: 'dotenv stg'},
        '.env.prd': {test_var: 'dotenv prd'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(fallbacks=fallbacks, override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]

def test_no_fallbacks(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.dev': {test_var: 'dotenv dev'},
        '.env.stg': {test_var: 'dotenv stg'},
        '.env.prd': {test_var: 'dotenv prd'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(fallbacks=[], override=True)
    assert os.getenv(test_var) is None

def test_no_fallbacks_and_dotenv_foo(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
        '.env.dev': {test_var: 'dotenv dev'},
        '.env.stg': {test_var: 'dotenv stg'},
        '.env.prd': {test_var: 'dotenv prd'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(fallbacks=[], override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]

def test_dotenv_foo_only(create_dotenv_files):
    os.environ[ds.default_var] = 'foo'
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)
    ds.load(fallbacks=fallbacks, override=True)
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]
