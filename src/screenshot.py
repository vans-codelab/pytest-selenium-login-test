from src.logger import logger
from src.paths import SCREENSHOT_FOLDER
import os
import time


def make_screenshot(name, webpage):
    """Makes a screenshot of the website and saves it in the screenshot folder."""

    # Create screenshot folder (if not available)
    if not os.path.exists(SCREENSHOT_FOLDER):
        logger.info("Screenshot folder does not exist.")
        os.makedirs(SCREENSHOT_FOLDER)
        logger.info("Screenshot folder is created.")

    # Define screenshot format
    timestamp = time.strftime("%Y-%m-%d_%H%M%S")
    file = f"{SCREENSHOT_FOLDER}/{name}_{timestamp}.png"

    # Capture screenshot
    logger.info("Make a screenshot: %s", file)
    webpage.save_screenshot(file)
