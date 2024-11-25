import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Set up a rotating logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5
    )
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
    
    return logger
