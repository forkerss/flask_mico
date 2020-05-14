"""
setup logger
"""
import os
import logging
import sys
from logging.handlers import RotatingFileHandler
from typing import TextIO

from app.settings import LOGDIR, SERVICE_ID

__all__ = ["logger", "setup_logger"]

FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'
LOGLEVELS = {
    'development': logging.DEBUG,
    'production': logging.INFO,
    'testing': logging.DEBUG
}

logger = logging.getLogger("TestMicroserviceAPI")
logger.propagate = False


def setup_logger(level: int = logging.DEBUG,
                 stream: TextIO = sys.stdout):
    # clear logging default handlers
    logging.getLogger().handlers.clear()
    logger.handlers.clear()
    # add logger format
    formatter = logging.Formatter(FORMAT, TIMESTAMP_FORMAT)
    # set logger handler
    if level == logging.INFO:
        # add rotaing file handler
        log_file_name = 'logger-%s.log' % SERVICE_ID
        log_file_str = os.path.join(LOGDIR, log_file_name)
        file_handler = RotatingFileHandler(
            filename=log_file_str,
            maxBytes=1024 * 1024 * 50,
            backupCount=5, encoding='utf-8')
        file_handler.suffix = "_%Y-%m-%d_%H.log"
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # default console handler
    console_handler = logging.StreamHandler(stream)
    console_handler.setLevel(logging.NOTSET)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # set level
    logger.setLevel(level)
