# Python Dotenv Switch

Wraps [python-dotenv](https://pypi.org/project/python-dotenv/) to enable
switching among multiple, environment-specific `.env` files.

## Usage

### Quick start

The fastest, easiest way to use `dotenv_switch` is to use the `auto` mode to
automatically load dotenv files upon import: `import dotenv_switch.auto`

Example:

```python
# Assuming $APP_ENV=prod and .env.prod contains
# A_VARIABLE=itsvalue

import dotenv_switch.auto

import os
os.getenv('A_VARIABLE')
>> itsvalue
```

The `auto` mode accepts all defaults:

* `APP_ENV` is the name of the environment variable that specifies the
  application environment.
* Load `.env.$APP_ENV` if it exists.
* If `.env.$APP_ENV` does not exist, fallback to loading `.env.test`, or if that
  doesn't exist, `.env`.
* If none of the above files exist, return successfully and raise no errors/exceptions.

For instructions on overriding the defaults, see [API](#api).

### API

#### load()

    import dotenv_switch
    dotenv_switch.load(var='APP_ENV', fallbacks=['.env.test','.env'], required=False, usecwd=False, **kwargs)

Parameters:

* `var` (str, optional) name of the env var specifying the desired environemnt (default is `APP_ENV`)
* `fallbacks` (list, optional) list of dotenv filenames to use if `var` is `None` or `.env.{var}` is
  not found (default is `['.env.test','.env']`)
* `required` (bool, optional) whether to raise an exception if no dotenv file is found (default is `False`)
* `usecwd` (bool, optional) `dotenv.find_dotenv()` param, with the same default, which will be
  passed to that function (default is `False`)
* `**kwargs` (optional) any remaining params will be passed to `dotenv.load_dotenv()`

Raises:

* `DotenvSwitchUnspecifiedFilesRequiredError` If required is `True`, but `var` is `None` or
  `.env.{var}` cannot be found, and fallbacks is `None` or empty.
* `DotenvSwitchFileNotFoundError` If `required` is `True` but no dotenv file can be found.

Returns

* `DotEnv`, the object returned by `dotenv.loadenv()`.

#### Package defaults

The default values of [load](#load) parameters are specified by these package variables:

    default_var = 'APP_ENV'
    default_fallbacks = ['.env.test', '.env']
    default_required = False
    default_usecwd = False

Resetting these package variables is another way to customize the behavior of `load()`.

#### auto modes

`dotenv_switch.auto` just calls `dotenv_switch.load()` after importing the package.
Overriding `load()` parameters and/or resetting package variable defaults allows for
easy creation of custom auto modes for convenient, one-line importing and loading.

## Testing

Pytest tests work by setting the active environment variable, then importing the
library to cause it to be invoked. This requires tests each be run in separate
processes to avoid contaminating each other's environments or import state. Run
pytest with the `--forked` flag to achieve this.

```shell
$ poetry run pytest --forked
```
