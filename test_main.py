from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="class")
def browser():
    browser = webdriver.Firefox()
    yield browser    # yield -> in caz executi ceva dupa test
    browser.close()

@pytest.fixture(scope="class")
def wait(browser):
   wait = WebDriverWait(browser, 10)
   return wait


class TestLogin:
   def test_login_with_bad_credentials(self, browser, wait):
      page = LoginPage(browser,wait) 
      products_page = page.login(user_name="standard_user), password="secret_sauce)
      login_page = products_page.logout()
      assert login_page.login_button_is_present()
#       browser.get("https://www.saucedemo.com/")
#       user_name_input = browser.find_element(By.ID, "user-name")
#       user_name_input.send_keys("locked_out_user")

#       password_input = browser.find_element(By.ID, "password")
#       password_input.send_keys("secret_sauce")

#       login_button = browser.find_element(By.ID, "login-button")
#       login_button.click()

#       assert wait.until(
#          EC.text_to_be_present_in_element(
#             (By.CSS_SELECTOR, ".error-message-container"),
#             "Epic sadface: Sorry, this user has been locked out.")
#       )

#    def test_login_with_good_credentials(self, browser, wait):
#       browser.get("https://www.saucedemo.com/")
#       user_name_input = browser.find_element(By.ID, "user-name")
#       user_name_input.send_keys("standard_user")

#       password_input = browser.find_element(By.ID, "password")
#       password_input.send_keys("secret_sauce")

#       login_button = browser.find_element(By.ID, "login-button")
#       login_button.click()

#       product_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
#       assert product_title.is_displayed()
#       assert product_title.text == "PRODUCTS"

#       menu_button = wait.until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
#       menu_button.click()

#       logout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logout_sidebar_link")))
#       logout_button.click()

#       login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
#       assert login_button.is_displayed()