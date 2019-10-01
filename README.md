# Python Dotenv Switch
Enables switching between sourced `.env` files based on the environment defined 
in `$APP_ENV`.

## Usage

Basic usage in Python - ensure the `$APP_ENV` environment variable is set
and a corresponding `.env.$APP_ENV` file exists.

If not set or empty, `$APP_ENV` defaults to `test`.

```python
# Assuming $APP_ENV=prod and .env.prod contains
# A_VARIABLE=itsvalue

import os
# Simply import it
import dotenv_switch

os.getenv('A_VARIABLE')
>> itsvalue
```

If `.env.$APP_ENV` does not exist, an exception will be thrown

```shell
# .env.prod does not exist!
$ APP_ENV=bogus python

>>> import dotenv_switch

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/mjb/src/experts/experts_dw/.venv/src/dotenv-switch/dotenv_switch/__init__.py", line 13, in <module>
    raise DotenvSwitchFileNotFoundError(app_env_file)
dotenv_switch.exceptions.DotenvSwitchFileNotFoundError: Dotenv file .env.bogus was not found
```

## Testing
Pytest tests work by setting the active environment variable then importing the 
library to cause it to be invoked. This requires tests each be run in separate 
processes to avoid contaminating each other's environments or import state. Run 
pytest with the `--forked` flag to achieve this.

```shell
$ poetry run pytest --forked
```
