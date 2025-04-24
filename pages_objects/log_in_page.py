from selenium.webdriver.common.by import By

from pages_objects.home_page import HomePage


class logInPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # objects in the page
    username_input_box_locator = (By.ID, "user-name")
    password_input_box_locator = (By.ID, "password")
    login_button_locator = (By.XPATH, "//input[@id='login-button']")

    # fuctions relaed to objects
    def username_input_box(self):
        return self.driver.find_element(*logInPage.username_input_box_locator)

    def password_input_box(self):
        return self.driver.find_element(*logInPage.password_input_box_locator)

    def login_button(self):
        self.driver.find_element(*logInPage.login_button_locator).click()
        return HomePage(self.driver, self.wait)