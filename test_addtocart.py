import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(10)

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert cart_badge.text == "1"
    print("✅ Add to cart test passed")
    driver.quit()

if __name__ == "__main__":
    test_add_to_cart()
