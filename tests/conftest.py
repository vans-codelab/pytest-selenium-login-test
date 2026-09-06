from src.logger import logger
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os


def pytest_addoption(parser):
    """Adds command line option '--headless' for pytest. If the test is started with 'pytest --headless',
    then the browser will open in headless mode (= without GUI)."""
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture
def browser(request):
    """When test case begins, start browser (Setup) and pass browser to test case.
    When test case ends, close browser (Teardown)."""
    testcase_name = request.node.name
    logger.info(f"----- START TEST CASE: {testcase_name} -----")
    logger.info("Calling fixture for browser().")

    # Browser options
    logger.info("Define browser options.")
    options = Options()

    # Headless mode (on/off)
    headless = request.config.getoption("--headless")
    logger.info(f"Checked if headless mode is requested. Result: headless == {headless}")

    if headless:
        options.add_argument("--headless=new")  # Browser in headless mode
        options.add_argument("--no-sandbox")  # Avoids sandbox problems on GitHub
        options.add_argument("--disable-dev-shm-usage")  # Avoids crashes due to memory problems
    else:
        options.add_argument("--start-maximized")  # Browser in fullscreen

    # ChromeDriver
    logger.info("Install ChromeDriver (if not available).")
    service = Service(ChromeDriverManager().install())

    # Start browser
    logger.info("Open browser.")
    driver = webdriver.Chrome(service=service, options=options)

    browser_name = driver.capabilities["browserName"].title()
    logger.info("Browser %s started.", browser_name)

    # Pass browser
    logger.info("Pass driver (= browser) to test case.")
    yield driver

    # Close browser
    logger.info("Close browser.")
    driver.quit()


@pytest.fixture
def valid_credentials():
    load_dotenv()
    username = os.environ.get("VALID_USERNAME", "tomsmith")
    password = os.environ.get("VALID_PASSWORD", "SuperSecretPassword!")
    return username, password


@pytest.fixture(scope="session", autouse=True)   # Called automatically when testrun starts
def start_message():
    logger.info("===== START TESTRUN =====")

