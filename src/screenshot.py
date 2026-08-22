from src.logger import logger
from src.paths import SCREENSHOT_FOLDER
import time


def make_screenshot(name, webpage):
    """Makes a screenshot of the website and saves it in the screenshot folder."""

    # Create Screenshot folder
    logger.info("Create screenshot folder (if not available)")
    SCREENSHOT_FOLDER.mkdir(parents=True, exist_ok=True)

    # Define screenshot format
    timestamp = time.strftime("%Y-%m-%d_%H%M%S")
    file = f"{SCREENSHOT_FOLDER}/{name}_{timestamp}.png"

    # Capture screenshot
    logger.info("Make a screenshot: %s", file)
    webpage.save_screenshot(file)
