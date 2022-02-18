from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, wait):
        self.browser = browser
        self.wait = wait 
    pass


class LoginPage(BasePage):
    user_name = (By.ID, "user-name")
    password = (By.ID, "password") 
    login_button = (By.ID, "login-button") 
    error_box = (By.CSS_SELECTOR, ".error-message-container")

    def login(self, user_name, password)
        user_name_input = self.browser.find_element(*self.user_name_locator)
        user_name_input.semd_keys(user_name)
        password_input = self.browser.find_element(*self.password)
        password_input.send_keys(password)
        login_button = self.browser.find_element(EC.element_to_be_clickable(*self.login_button_locater))
        login_button.click()
        return ProductsPage(self.browser, self.wait)

    def login_button_is_clickable(self):
        return EC.element_to_be_clickable(*self.login_locater


class ProductsPage:
    product_title_locator = (By.CLASS_NAME, "title")
    hamburger_button_locator = (By.ID, "react-burger-menu-btn")
    log_out_button_locator = (By.CSS_SELECTOR, "#lougout_sidebar_link")

    def logout(self):
        pass