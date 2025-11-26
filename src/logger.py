from src.paths import LOG_FOLDER
import logging
import os


# Create log folder (if not available)
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

# Define logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# If no handler is added to logger yet (avoids multiple logging)
if not logger.handlers:
    # Define Filehandler (for writing logs into log file (.txt))
    filehandler = logging.FileHandler(filename=f"{LOG_FOLDER}/login.log", mode="w")
    filehandler.setLevel(logging.INFO)
    logger.addHandler(filehandler)
    # Define log format
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    filehandler.setFormatter(fmt)

logger.info("Logger initialized.")