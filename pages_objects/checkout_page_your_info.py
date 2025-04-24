from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages_objects.checkout_page_overview import Overview_page


class your_info:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    first_name_locator = (By.XPATH, "//input[@id='first-name']")
    last_name_locator = (By.XPATH, "//input[@id='last-name']")
    postal_code_locator = (By.XPATH, "//input[@id='postal-code']")
    continue_button_locator = (By.XPATH, "//input[@id='continue']")

    def first_name(self):
        return self.wait.until(EC.element_to_be_clickable(your_info.first_name_locator))

    def last_name(self):
        return self.wait.until(EC.element_to_be_clickable(your_info.last_name_locator))

    def postal_code(self):
        return self.wait.until(EC.element_to_be_clickable(your_info.postal_code_locator))

    def continue_button(self):
        self.wait.until(EC.element_to_be_clickable(your_info.continue_button_locator)).click()
        return Overview_page(self.driver, self.wait)
