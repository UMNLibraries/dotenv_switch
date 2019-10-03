# Python Dotenv Switch
Enables switching between sourced `.env` files based on the environment defined
in `$APP_ENV`. E.g. if `$APP_ENV=prod`, load `.env.prod`

## Usage

### Basic automatic loading
Basic automatic usage in Python - ensure the `$APP_ENV` environment variable is
set and a corresponding `.env.$APP_ENV` file exists.

If not set or empty, `$APP_ENV` defaults to `test`.

```python
# Assuming $APP_ENV=prod and .env.prod contains
# A_VARIABLE=itsvalue

import os

# Simply import the auto mode
import dotenv_switch.auto

os.getenv('A_VARIABLE')
>> itsvalue
```

If `.env.$APP_ENV` does not exist, variables will be empty but no exception will
be thrown.

### Automatic loading with REQUIRED config file

Like basic automatic loading but if `.env.$APP_ENV` does not exist, an exception
will be thrown

```shell
# .env.bogus does not exist!
$ APP_ENV=bogus python
```

```python
# Import the auto_required mode
import dotenv_switch.auto_required

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/mjb/src/experts/experts_dw/.venv/src/dotenv-switch/dotenv_switch/__init__.py", line 13, in <module>
    raise DotenvSwitchFileNotFoundError(app_env_file)
dotenv_switch.exceptions.DotenvSwitchFileNotFoundError: Dotenv file .env.bogus was not found
```

### Advanced usage
Rather than auto mode accepting defaults for the environment variable to consult
and the default environment if unset, you may set these options.

```shell
# Assuming var $MY_ENV=stage is set and .env.stage contains
A_VARIABLE="staging variable"
```

```python
import os

# Load the module (not auto mode)
import dotenv_switch

# Tell dotenv_switch to read the environment from $MY_ENV
dotenv_switch.load(var='MY_ENV')
os.getenv('A_VARIABLE')
>>> "staging variable"

# Tell dotenv_switch to read from $OTHER_ENV and if not set, default to .env.dev
dotenv_switch.load(var='OTHER_ENV', default_env='dev')

# Same, but also throw an exception if .env.dev does not exist
dotenv_switch.load(var='OTHER_ENV', default_env='dev', required=True)
```

## Testing
Pytest tests work by setting the active environment variable then importing the
library to cause it to be invoked. This requires tests each be run in separate
processes to avoid contaminating each other's environments or import state. Run
pytest with the `--forked` flag to achieve this.

```shell
$ poetry run pytest --forked
```
