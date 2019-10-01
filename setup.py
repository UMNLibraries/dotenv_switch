# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['dotenv_switch']

package_data = \
{'': ['*']}

install_requires = \
['python_dotenv>=0.10.3,<0.11.0']

setup_kwargs = {
    'name': 'dotenv-switch',
    'version': '0.0.1',
    'description': 'Switch between sourcing .env files based on $APP_ENV environment variable',
    'long_description': '# Python Dotenv Switch\nEnables switching between sourced `.env` files based on the environment defined \nin `$APP_ENV`.\n\n## Usage\n\nBasic usage in Python - ensure the `$APP_ENV` environment variable is set\nand a corresponding `.env.$APP_ENV` file exists.\n\nIf not set or empty, `$APP_ENV` defaults to `test`.\n\n```python\n# Assuming $APP_ENV=prod and .env.prod contains\n# A_VARIABLE=itsvalue\n\nimport os\n# Simply import it\nimport dotenv_switch\n\nos.getenv(\'A_VARIABLE\')\n>> itsvalue\n```\n\nIf `.env.$APP_ENV` does not exist, an exception will be thrown\n\n```shell\n# .env.prod does not exist!\n$ APP_ENV=prod python\n\n>>> import dotenv_switch\n\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  File "/home/mjb/src/experts/dotenv_switch/dotenv_switch/__init__.py", line 9, in <module>\n    load_dotenv(find_dotenv(filename=app_env_file, raise_error_if_not_found=True))\n  File "/home/mjb/.pyenv/versions/3.6.3/lib/python3.6/site-packages/dotenv/main.py", line 269, in find_dotenv\n    raise IOError(\'File not found\')\nOSError: File not found\n```\n',
    'author': 'Michael Berkowski',
    'author_email': 'mjb@umn.edu',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.3,<4.0.0',
}


setup(**setup_kwargs)
