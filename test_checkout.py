from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    driver.find_element(By.ID, "first-name").send_keys("Rujiphas")
    driver.find_element(By.ID, "last-name").send_keys("Pakornmaneekul")
    driver.find_element(By.ID, "postal-code").send_keys("10250")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)
    assert "Thank you for your order!" in driver.page_source
    print("✅ Checkout test passed")
    driver.quit()

if __name__ == "__main__":
    test_checkout()
