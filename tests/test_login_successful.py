from src.logger import logger
from src.login import Login
from src.screenshot import make_screenshot


def test_login_successful(browser):
    login = Login(browser)
    login.open_website()
    logger.info("Website is opened.")

    make_screenshot("01_Before_Login", login.driver)
    logger.info("Screenshot is saved.")

    username = "tomsmith"
    password = "SuperSecretPassword!"
    login.enter_credentials(username, password)
    logger.info("Username and password are entered.")

    assert login.is_logged_in(), "Login was not successful."
    logger.info("Login was successful.")

    make_screenshot("02_After_Login", browser)
    logger.info("Screenshot is saved.")



