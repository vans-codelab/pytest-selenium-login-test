from src.paths import LOG_FOLDER
import logging
import os

# LOG_FOLDER = "../tests/logs"

if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# If no handler is added to logger yet (avoids multiple logging)
if not logger.handlers:
    # Filehandler - Writes logs into log file (.txt)
    filehandler = logging.FileHandler(filename=f"{LOG_FOLDER}/login.log", mode="w")
    filehandler.setLevel(logging.INFO)
    logger.addHandler(filehandler)

    # Format of Log
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    filehandler.setFormatter(fmt)


logger.info("Logger initialized.")