import logging
import os
from pathlib import Path

from utils.timeResponser import time_responser

class Logger(logging.Logger):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.setLevel(logging.DEBUG)
        self.propagate = False

        self.addHandler(ConsoleHandler())
        self.addHandler(FileHandler())

    def debug(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.DEBUG):
            self._log(logging.DEBUG, msg, args, **kwargs)

    def info(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.INFO):
            self._log(logging.INFO, msg, args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.WARNING):
            self._log(logging.WARNING, msg, args, **kwargs)

    def error(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.ERROR):
            self._log(logging.ERROR, msg, args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        if self.isEnabledFor(logging.CRITICAL):
            self._log(logging.CRITICAL, msg, args, **kwargs)



class ConsoleHandler(logging.StreamHandler):
    def __init__(self, level=logging.DEBUG):
        super().__init__()
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(level)


class FileHandler(logging.FileHandler):
    def __init__(self):

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)  # Create folder if it doesn't exist

        filename = f"logfile_{time_responser('datetime')}.log"
        filepath = Path(log_dir, filename)

        super().__init__(filepath, encoding="UTF-8")
        
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%m/%d/%Y %H:%M:%S",
        )
        self.setFormatter(formatter)
        self.setLevel(logging.INFO)