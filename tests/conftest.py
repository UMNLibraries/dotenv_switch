import pytest
import os

@pytest.fixture()
def create_dotenv_files():
    def _create_dotenv_files(path, dotenv_file_metadata={}):
        dotenv_files = []
        for dotenv_filename, env_vars in dotenv_file_metadata.items():
            dotenv_file = path / dotenv_filename 
            for k, v in env_vars.items():
                dotenv_file.write_text(f'{k}="{v}"\n')
            dotenv_files.append(dotenv_file)
        return dotenv_files
    return _create_dotenv_files

@pytest.fixture()
def delete_dotenv_files():
    def _delete_dotenv_files(dotenv_files):
        for dotenv_file in dotenv_files:
            dotenv_file.unlink()
    return _delete_dotenv_files

