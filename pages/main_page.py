from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    FIELD_SEARCH = (By.XPATH, "//*[@placeholder = 'Поиск']")
    BUTTON_NOT_NOW = (By.XPATH, "//button[text() = 'Не сейчас']")

    def _verify_page(self):
        self.on_this_page(self.BUTTON_NOT_NOW)

    def type_in_search_field(self, text):
        self.type_in(self.FIELD_SEARCH, text)

    def click_not_now_button(self):
        self.click_on(self.BUTTON_NOT_NOW)

    def click_result_with_text(self, text):
        RESULT = (By.XPATH, "//span[text() = '{}']".format(text))
        self.click_on(RESULT)
