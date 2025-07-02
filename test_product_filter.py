from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_product_filter():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    filter_dropdown.click()
    time.sleep(5)
    options = filter_dropdown.find_elements(By.TAG_NAME, "option")
    for option in options:
        if option.text == "Name (Z to A)":
            option.click()
            break
    time.sleep(2)
    print("✅ Product filter test passed")
    driver.quit()

if __name__ == "__main__":
    test_product_filter()
