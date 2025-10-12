from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


def save_screenshot(name):
    if not os.path.exists("./screenshots"):
        os.makedirs("./screenshots")

    timestamp = time.strftime("%Y-%m-%d_%H%M%S")
    file = f"./screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(file)


# Open webpage in Browser
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')

# Wait until elements are loaded
wait = WebDriverWait(driver, timeout=10)
wait.until(EC.visibility_of_element_located((By.ID, "username")))

# Make a screenshot
save_screenshot("01_Before_Login")

# User input: Username, Password
username = driver.find_element(By.ID, "username")
input_username = "tomsmith"
username.send_keys(input_username)

password = driver.find_element(By.ID, "password")
input_password = "SuperSecretPassword!"
password.send_keys(input_password)

# Login: Confirm Button
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Check confirmation & make a screenshot in case of an error
readout_message = driver.find_element(By.ID, "flash").text
message = readout_message.strip().replace("×","")

try:
    assert "logged into a secure area!" in message.lower()
except AssertionError:
    save_screenshot("02_Error_After_Login")
    raise

# Close Browser
driver.quit()