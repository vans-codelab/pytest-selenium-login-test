from src.logger import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


LOG_FOLDER = "./logs"


@pytest.fixture
def browser(request):
    """When test case begins, start browser (Setup) and pass browser to test case.
    When test case ends, close browser (Teardown)."""
    testcase_name = request.node.name
    logger.info(f"----- START TEST CASE: {testcase_name} -----")

    logger.info("Calling fixture for browser().")
    logger.info("[Setup]: Start browser")
    options = Options()
    options.add_argument("--start-maximized")  # Open Browser in fullscreen
    driver = webdriver.Chrome(options=options)

    browser_name = driver.capabilities["browserName"].title()
    logger.info("Browser %s started.", browser_name)

    logger.info("[Setup] Pass driver (browser) to test case.")
    yield driver

    logger.info("[Teardown]: Close browser.")
    driver.quit()


@pytest.fixture(scope="session", autouse=True)   # Called automatically when testrun starts
def start_message():
    logger.info("===== START TESTRUN =====")

