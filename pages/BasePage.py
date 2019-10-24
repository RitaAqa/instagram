class BasePage()
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(ecpected_condition, message = "Unable to locate element")

    def click_on(self, locator):
        self.get_element(locator).click()

    def type_in(self, locator, text):
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(text)

                                                    







