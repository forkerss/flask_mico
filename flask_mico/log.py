"""
setup logger
"""
import logging
import os
from logging.handlers import RotatingFileHandler

FORMAT = '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s'
TIMESTAMP_FORMAT = '%Y-%m-%d %H:%M:%S %z'


logger = logging.getLogger("TestMicroserviceAPI")
logger.propagate = False


def setup_logger(level, logdir, service_name):
    # process level
    if isinstance(level, bool) and level is True:
        level = logging.DEBUG
    else:
        level = logging.INFO
    # clear logging default handlers
    logging.getLogger().handlers.clear()
    logger.handlers.clear()
    # add logger format
    formatter = logging.Formatter(FORMAT, TIMESTAMP_FORMAT)
    # set logger handler
    if level == logging.INFO:
        # add rotaing file handler
        log_file_name = 'logger-%s.log' % service_name
        log_file_str = os.path.join(logdir, log_file_name)
        file_handler = RotatingFileHandler(
            filename=log_file_str,
            maxBytes=1024 * 1024 * 50,
            backupCount=5, encoding='utf-8')
        file_handler.suffix = "_%Y-%m-%d_%H.log"
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # default console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.NOTSET)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    # set level
    logger.setLevel(level)
