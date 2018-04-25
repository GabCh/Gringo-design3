class Logger:
    def info(self, message: str):
        pass

    def warn(self, message: str):
        pass

    def debug(self, message: str):
        pass

    def error(self, message: str):
        pass


class LogLevel:
    """Logging sensitivity. While testing, use lower levels to get more insight."""
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3

    strings = {DEBUG: "DEBUG", INFO: "INFO", WARNING: "WARNING", ERROR: "ERROR"}

    @staticmethod
    def to_string(log_level: int) -> str:
        return LogLevel.strings[log_level]
