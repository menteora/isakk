import time
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler
from enum import Enum

class LogWrapper:

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        # self.handler = create_log_timebased(logfile)
        # self.logger.addHandler(handler_file)

    def setHanderFormatter(self, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        formatter = logging.Formatter(format)
        self.handler.setFormatter(formatter)

    def setHandlerLevelDebug(self):
        self.logger.setLevel(logging.DEBUG)
        self.handler.setLevel(logging.DEBUG)

    def setHandlerFileTimebased(self, path, when="D"):

        self.handler = TimedRotatingFileHandler(path,
                                        when=when,
                                        interval=1,
                                        backupCount=5)
        self.logger.addHandler(self.handler)
        
    def setHandlerFileBytebased(self, path, byte=1000000):

        self.handler = RotatingFileHandler(path, maxBytes=byte,
                                    backupCount=5)
        self.logger.addHandler(self.handler)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
