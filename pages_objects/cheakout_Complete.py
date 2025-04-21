from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class checkoutComplete:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def URL_get(self):
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/checkout-complete.html"))
        return self.driver.current_url