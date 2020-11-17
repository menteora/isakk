import time
import logging
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler

def create_handler_file_timebased(path, when="D"):

    handler = TimedRotatingFileHandler(path,
                                       when=when,
                                       interval=1,
                                       backupCount=5)
    return handler
    
def create_handler_file_bytebased(path, byte=1000000):

    handler = RotatingFileHandler(path, maxBytes=byte,
                                  backupCount=5)
    return  handler
