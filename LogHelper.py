import time
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def create_timed_rotating_log_timebased(path, when="D"):

    handler = TimedRotatingFileHandler(path,
                                       when=when,
                                       interval=1,
                                       backupCount=5)
    logger.addHandler(handler)
    return logger
    
def create_timed_rotating_log_bytebased(path, byte=1000000):

    handler = RotatingFileHandler(path, maxBytes=byte,
                                  backupCount=5)
    logger.addHandler(handler)
    return logger