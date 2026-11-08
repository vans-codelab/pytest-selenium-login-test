from src.logger import logger
from src.login import Login
from src.screenshot import make_screenshot
import pytest

# Placeholder in parametrize list. Valid value will be provided from fixture during test run.
USE_VALID_CREDENTIAL = None


def test_login_succeeds_with_valid_credentials(browser, base_url, valid_credentials):
    login = Login(browser, base_url)
    login.open_website()
    logger.info("Website is opened.")

    make_screenshot("01_before_login_valid", login.driver)
    logger.info("Screenshot is saved.")

    login.enter_credentials(valid_credentials["username"], valid_credentials["password"])
    logger.info("Username and password are entered.")

    make_screenshot("02_after_login_valid", browser)
    logger.info("Screenshot is saved.")

    expected_message = "You logged into a secure area!"
    logger.info("Expected message: '%s'", expected_message)
    assert login.login_message() == expected_message
    logger.info("Login was successful.")


@pytest.mark.parametrize("username, password, expected_message", [
    ("INVALID_USERNAME", USE_VALID_CREDENTIAL, "Your username is invalid!"),
    (USE_VALID_CREDENTIAL, "INVALID_PASSWORD", "Your password is invalid!"),
    ("INVALID_USERNAME", "INVALID_PASSWORD", "Your username is invalid!"),
    ("", USE_VALID_CREDENTIAL, "Your username is invalid!"),
    (USE_VALID_CREDENTIAL, "", "Your password is invalid!"),
    ("", "", "Your username is invalid!"),
], ids=["wrong_username", "wrong_password", "wrong_username_password",
        "empty_username", "empty_password", "empty_username_password"])
def test_login_fails_with_invalid_credentials(request, browser, base_url, valid_credentials,
                                              username, password, expected_message):
    test_id = request.node.callspec.id

    login = Login(browser, base_url)
    login.open_website()
    logger.info("Website is opened.")

    make_screenshot(f"01_before_login_invalid_{test_id}", login.driver)
    logger.info("Screenshot is saved.")

    if username is USE_VALID_CREDENTIAL:
        username = valid_credentials["username"]
    if password is USE_VALID_CREDENTIAL:
        password = valid_credentials["password"]

    login.enter_credentials(username, password)
    logger.info("Username and password are entered.")

    make_screenshot(f"02_after_login_invalid_{test_id}", browser)
    logger.info("Screenshot is saved.")

    logger.info("Expected message: '%s'", expected_message)
    assert login.login_message() == expected_message
    logger.info("Login failed (as expected).")
