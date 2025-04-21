from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Cart:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    checkout_button_locator = (By.XPATH, "//button[@id='checkout']")

    def checkout_button(self):
        return self.wait.until(EC.element_to_be_clickable(Cart.checkout_button_locator))