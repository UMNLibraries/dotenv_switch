class DotenvSwitchFileNotFoundError(Exception):
    def __init__(self, filename):
        self.message = f"Dotenv file {filename} was not found"
        super().__init__(self.message)

