import logging
import os

def get_logger(name, log_file='logs/run.log'):
    logger = logging.getLogger(name)

    # Prevent adding multiple handlers in case of repeated calls
    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create 'logs' directory if it doesn't exist
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        # File handler - overwrites the log file each time
        file_handler = logging.FileHandler(log_file, mode='w')  # 'w' for overwrite
        file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(file_formatter)

        # Stream handler (optional, shows logs in console)
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(file_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
