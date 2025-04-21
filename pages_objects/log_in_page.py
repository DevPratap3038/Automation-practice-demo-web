from selenium.webdriver.common.by import By


class logInPage:
    def __init__(self, driver):
        self.driver = driver

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
        return self.driver.find_element(*logInPage.login_button_locator)