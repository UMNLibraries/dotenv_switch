import errno
import os

class DotenvSwitchFileNotFoundError(FileNotFoundError):
    def __init__(self, filename):
        super().__init__(errno.ENOENT, os.strerror(errno.ENOENT), filename)
