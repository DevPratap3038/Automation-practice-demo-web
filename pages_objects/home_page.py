from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    products_locator = (By.XPATH, "//div[@class='inventory_item']")
    button_backpack_locator = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    button_fleece_jacket_locator = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
    shopping_cart_button_locator = (By.XPATH, "//a[@class='shopping_cart_link']")

    def Products(self):
        return self.wait.until(EC.visibility_of_all_elements_located(HomePage.products_locator))

    def button_backpack(self):
        return self.wait.until(EC.element_to_be_clickable(HomePage.button_backpack_locator))

    def button_fleece_jacket(self):
        return self.wait.until(EC.element_to_be_clickable(HomePage.button_fleece_jacket_locator))

    def shopping_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable((HomePage.shopping_cart_button_locator)))

