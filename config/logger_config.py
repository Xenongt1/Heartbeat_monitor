import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file='logs/app.log', level=logging.INFO):
    """Function to setup as many loggers as you want"""
    
    # Ensure logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(name)s] %(message)s')

    # File handler
    handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid duplicate handlers if setup is called multiple times
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console_handler)

    return logger
