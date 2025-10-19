from src.logger import logger
import os
import time


SCREENSHOT_FOLDER = "./screenshots"


def make_screenshot(name, webpage):
    """Makes a screenshot of the website and saves it in the screenshot folder."""
    if not os.path.exists(SCREENSHOT_FOLDER):
        logger.info("Screenshot folder does not exist.")
        os.makedirs(SCREENSHOT_FOLDER)
        logger.info("Screenshot folder is created.")

    timestamp = time.strftime("%Y-%m-%d_%H%M%S")
    file = f"{SCREENSHOT_FOLDER}/{name}_{timestamp}.png"
    logger.info("Make a screenshot: %s", file)
    webpage.save_screenshot(file)
