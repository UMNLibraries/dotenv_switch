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
$ APP_ENV=prod python

>>> import dotenv_switch

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/mjb/src/experts/dotenv_switch/dotenv_switch/__init__.py", line 9, in <module>
    load_dotenv(find_dotenv(filename=app_env_file, raise_error_if_not_found=True))
  File "/home/mjb/.pyenv/versions/3.6.3/lib/python3.6/site-packages/dotenv/main.py", line 269, in find_dotenv
    raise IOError('File not found')
OSError: File not found
```
