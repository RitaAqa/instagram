from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    FIELD_USERNAME = (By.NAME, "username")
    FIELD_PASSWORD = (By.NAME, "password")
    BUTTON_LOGIN = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.type_in(self.FIELD_USERNAME, username)

    def enter_password(self, password):
        self.type_in(self.FIELD_PASSWORD, password)

    def click_login(self):
        self.click_on(self.BUTTON_LOGIN)

