import os
import pathlib

def test_defaults_no_app_env(create_dotenv_files, delete_dotenv_files):
    if 'APP_ENV' in os.environ:
        os.environ.pop('APP_ENV')

    test_var = 'TEST_VAR'
    dotenv_file_metadata = {
        '.env.test': {test_var: 'dotenv test'},
        '.env': {test_var: 'dotenv'},
    }
    dotenv_files = create_dotenv_files(pathlib.Path.cwd(), dotenv_file_metadata)

    import dotenv_switch
    dotenv_switch.load()
    assert os.getenv(test_var) == dotenv_file_metadata['.env.test'][test_var]

    delete_dotenv_files(dotenv_files)
