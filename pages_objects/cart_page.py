from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages_objects.checkout_page_your_info import your_info


class Cart:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    checkout_button_locator = (By.XPATH, "//button[@id='checkout']")

    def checkout_button(self):
        self.wait.until(EC.element_to_be_clickable(Cart.checkout_button_locator)).click()
        return your_info(self.driver, self.wait)