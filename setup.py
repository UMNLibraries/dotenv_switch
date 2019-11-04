# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['dotenv_switch', 'dotenv_switch.auto']

package_data = \
{'': ['*']}

install_requires = \
['python_dotenv>=0.10.3,<0.11.0']

setup_kwargs = {
    'name': 'dotenv-switch',
    'version': '0.1.0',
    'description': 'Switch between sourcing .env files based on $APP_ENV environment variable',
    'long_description': "# Python Dotenv Switch\n\nWraps [python-dotenv](https://pypi.org/project/python-dotenv/) to enable\nswitching among multiple, environment-specific `.env` files.\n\n## Usage\n\n### Quick start\n\nThe fastest, easiest way to use `dotenv_switch` is to use the `auto` mode to\nautomatically load dotenv files upon import: `import dotenv_switch.auto`\n\nExample:\n\n```python\n# Assuming $APP_ENV=prod and .env.prod contains\n# A_VARIABLE=itsvalue\n\nimport dotenv_switch.auto\n\nimport os\nos.getenv('A_VARIABLE')\n>> itsvalue\n```\n\nThe `auto` mode accepts all defaults:\n\n* `APP_ENV` is the name of the environment variable that specifies the\n  application environment.\n* Load `.env.$APP_ENV` if it exists.\n* If `.env.$APP_ENV` does not exist, fallback to loading `.env.test`, or if that\n  doesn't exist, `.env`.\n* If none of the above files exist, return successfully and raise no errors/exceptions.\n\nFor instructions on overriding the defaults, see [API](#api).\n\n### API\n\n#### load()\n\n    import dotenv_switch\n    dotenv_switch.load(var='APP_ENV', fallbacks=['.env.test','.env'], required=False, usecwd=False, **kwargs)\n\nParameters:\n\n* `var` (str, optional) name of the env var specifying the desired environemnt (default is `APP_ENV`)\n* `fallbacks` (list, optional) list of dotenv filenames to use if `var` is `None` or `.env.{var}` is\n  not found (default is `['.env.test','.env']`)\n* `required` (bool, optional) whether to raise an exception if no dotenv file is found (default is `False`)\n* `usecwd` (bool, optional) `dotenv.find_dotenv()` param, with the same default, which will be\n  passed to that function (default is `False`)\n* `**kwargs` (optional) any remaining params will be passed to `dotenv.load_dotenv()`\n\nRaises:\n\n* `DotenvSwitchUnspecifiedFilesRequiredError` If required is `True`, but `var` is `None` or\n  `.env.{var}` cannot be found, and fallbacks is `None` or empty.\n* `DotenvSwitchFileNotFoundError` If `required` is `True` but no dotenv file can be found.\n\nReturns\n\n* `DotEnv`, the object returned by `dotenv.loadenv()`.\n\n#### Package defaults\n\nThe default values of [load](#load) parameters are specified by these package variables:\n\n    default_var = 'APP_ENV'\n    default_fallbacks = ['.env.test', '.env']\n    default_required = False\n    default_usecwd = False\n\nResetting these package variables is another way to customize the behavior of `load()`.\n\n#### auto modes\n\n`dotenv_switch.auto` just calls `dotenv_switch.load()` after importing the package.\nOverriding `load()` parameters and/or resetting package variable defaults allows for\neasy creation of custom auto modes for convenient, one-line importing and loading.\n\n## Testing\n\nPytest tests work by setting the active environment variable, then importing the\nlibrary to cause it to be invoked. This requires tests each be run in separate\nprocesses to avoid contaminating each other's environments or import state. Run\npytest with the `--forked` flag to achieve this.\n\n```shell\n$ poetry run pytest --forked\n```\n",
    'author': 'Michael Berkowski',
    'author_email': 'mjb@umn.edu',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.3,<4.0.0',
}


setup(**setup_kwargs)
