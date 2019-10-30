import os
import pathlib

def test_defaults_app_env_foo(create_dotenv_files, delete_dotenv_files):
    os.environ['APP_ENV'] = 'foo'

    test_var = 'TEST_VAR'
    dotenv_file_metadata = {
        '.env.foo': {test_var: 'dotenv foo'},
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)

    import dotenv_switch
    dotenv_switch.load()
    assert os.getenv(test_var) == dotenv_file_metadata['.env.foo'][test_var]

    delete_dotenv_files(dotenv_files)
