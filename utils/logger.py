import logging

from functools import wraps


def log_extra_args(func):
    """
    A decorator to handle extra keyword arguments.
    """
    @wraps(func)
    def wrapper(self, msg, *args, **kwargs):
        extra_info = kwargs
        return func (self, msg, *args, extra = extra_info)
    return wrapper


class Logger(logging.Logger):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.setLevel(logging.DEBUG)
        self.propagate = False

        self.addHandler(ConsoleHandler())
        self.addHandler(FileHandler())

    @log_extra_args
    def debug(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.DEBUG):
            self._log(logging.DEBUG, msg, args, **kwargs)

    @log_extra_args
    def info(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.INFO):
            self._log(logging.INFO, msg, args, **kwargs)

    @log_extra_args
    def warning(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.WARNING):
            self._log(logging.WARNING, msg, args, **kwargs)

    @log_extra_args
    def error(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.ERROR):
            self._log(logging.ERROR, msg, args, **kwargs)

    @log_extra_args
    def critical(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.CRITICAL):
            self._log(logging.CRITICAL, msg, args, **kwargs)



class ConsoleHandler(logging.StreamHandler):
    def __init__(self, level=logging.DEBUG):
        super().__init__()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s - %(extra)s",
            datefmt="%m/%d/%Y %H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(level)


class FileHandler(logging.FileHandler):
    def __init__(self):
        super().__init__("logfile.log", encoding="UTF-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s - %(extra)s",
            datefmt="%m/%d/%Y %H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(logging.INFO)