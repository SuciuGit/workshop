from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_demo():
    browser = webdriver.Firefox()
    wait = WebDriverWait(browser, 10)
    browser.get('https://saucedemo.com/')

    user_name_input = browser.find_element(By.ID,"user-name")
    user_name_input.send_keys("standard_user")
    password_input = browser.find_element(By.ID,"password")
    password_input.send_keys("secret_sauce")
    login_button = browser.find_element(By.ID,"login-button")
    login_button.click()

    product_title = wait.until(EC.visibility_of_element_locate((By.CLASS_NAME,"title")))
    assert product_title.is_displayed()
    assert product_title.text == "PRODUCTS"

    menu_button = browser.find_element(By.CSS_SELECTOR, "#react-burger-menu-btn")
    menu_button.click()
    logout_button = ait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
    logout_button.click()
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    assert login_button.is_displayed
    el = webdriver
    browser.quit()
