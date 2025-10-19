from src.logger import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://the-internet.herokuapp.com/login"
        logger.info("Login class initialized.")

    def open_website(self):
        """Opens website and wait until it is loaded."""
        logger.info("Open website: %s", self.url)
        self.driver.get(self.url)
        logger.info("Wait until elements on website are loaded.")
        wait = WebDriverWait(self.driver, timeout=10)
        wait.until(ec.visibility_of_element_located((By.ID, "username")))

    def enter_credentials(self, username, password):
        """Enters username and password, then confirms login button."""
        logger.info("Enter username: %s", username)
        field_username = self.driver.find_element(By.ID, "username")
        field_username.send_keys(username)
        logger.info("Enter password: ***")
        field_password = self.driver.find_element(By.ID, "password")
        field_password.send_keys(password)
        logger.info("Confirm login button.")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

    def is_logged_in(self):
        """Checks if login was successful"""
        raw_message = self.driver.find_element(By.ID, "flash").text
        message = raw_message.replace("×", "").strip()
        logger.info('Message after login: "%s"', message)
        return "logged into a secure area" in message.lower()  # returns True/False


