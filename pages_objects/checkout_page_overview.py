from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages_objects.cheakout_Complete import checkoutComplete


class Overview_page:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    finish_button_locator = (By.XPATH, "//button[@id='finish']")

    def finish_button(self):
        self.wait.until(EC.element_to_be_clickable(Overview_page.finish_button_locator)).click()
        return checkoutComplete(self.driver, self.wait)