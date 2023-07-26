import logging


class logger_class:
    def __init__(self, logger_name, level, path):
        self.logger_name = logger_name
        self.level = level
        self.path = path

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s %(message)s")
        self.logger = logging.getLogger(self.logger_name)
        self.logger.setLevel(self.level)
        handler = logging.FileHandler(self.path)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
