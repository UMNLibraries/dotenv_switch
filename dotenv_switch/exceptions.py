import errno
import os

class DotenvSwitchFileNotFoundError(FileNotFoundError):
    def __init__(self, filenames_not_found):
        super().__init__(errno.ENOENT, 'No such file(s)', ', '.join(filenames_not_found))

class DotenvSwitchUnspecifiedFilesRequiredError(ValueError):
    def __init__(self):
        super().__init__('dotenv file required but no dovenv filenames specified')
