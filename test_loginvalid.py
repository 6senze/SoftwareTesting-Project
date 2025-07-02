from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_login_valid():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "inventory" in driver.current_url
    print("✅ Valid login passed")
    driver.quit()

if __name__ == "__main__":
    test_login_valid()
