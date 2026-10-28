from src.logger import logger
from src.login import Login
from src.screenshot import make_screenshot
import pytest

def test_login_succeeds_with_valid_credentials(browser, base_url, valid_credentials):
    login = Login(browser, base_url)
    login.open_website()
    logger.info("Website is opened.")

    make_screenshot("01_before_login_valid", login.driver)
    logger.info("Screenshot is saved.")

    username, password = valid_credentials
    login.enter_credentials(username, password)
    logger.info("Username and password are entered.")

    make_screenshot("02_after_login_valid", browser)
    logger.info("Screenshot is saved.")

    assert login.login_message() == "You logged into a secure area!"
    logger.info("Login was successful.")


@pytest.mark.parametrize("username, password, expected_message", [
    ("INVALID_USERNAME", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "INVALID_PASSWORD", "Your password is invalid!"),
    ("INVALID_USERNAME", "INVALID_PASSWORD", "Your username is invalid!"),
    ("", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "", "Your password is invalid!"),
    ("", "", "Your username is invalid!"),
], ids=["wrong_username", "wrong_password", "wrong_username_password",
        "empty_username", "empty_password", "empty_username_password"])

def test_login_fails_with_invalid_credentials(request, browser, base_url, username, password, expected_message):
    test_id = request.node.callspec.id

    login = Login(browser, base_url)
    login.open_website()
    logger.info("Website is opened.")

    make_screenshot(f"01_before_login_invalid_{test_id}", login.driver)
    logger.info("Screenshot is saved.")

    login.enter_credentials(username, password)
    logger.info("Username and password are entered.")

    make_screenshot(f"02_after_login_invalid_{test_id}", browser)
    logger.info("Screenshot is saved.")

    assert login.login_message() == expected_message
    logger.info("Login failed (as expected).")
