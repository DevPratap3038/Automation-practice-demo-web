import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from utilites.baseClass import baseclass
from pages_objects.log_in_page import logInPage
from pages_objects.home_page import HomePage
from pages_objects.cart_page import Cart
from pages_objects.checkout_page_your_info import your_info
from pages_objects.checkout_page_overview import Overview_page
from pages_objects.cheakout_Complete import checkoutComplete



class Test_class_01(baseclass):
    def test_def_01(self):

        #object of Log_In_page
        Log_In_page = logInPage(self.driver)

        wait = WebDriverWait(self.driver, 5)

        # valid credencials
        user_name = "standard_user"
        pass_word = "secret_sauce"

        # home page actions
        Log_In_page.username_input_box().send_keys(user_name)
        Log_In_page.password_input_box().send_keys(pass_word)
        Log_In_page.login_button().click()

        # to handle the password change manager
        # time.sleep(5)
        # oject of homepage
        Homepage = HomePage(self.driver, wait)

        Homepage.button_backpack().click()
        Homepage.button_fleece_jacket().click()
        Homepage.shopping_cart_button().click()
        # time.sleep(3)

        # now in cart
        # Cart_page object
        Cart_page = Cart(self.driver,wait)
        Cart_page.checkout_button().click()

        # now in your information (cheakout)
        Your_Info_page = your_info(self.driver,wait)
        Your_Info_page.first_name().send_keys("hari")
        Your_Info_page.last_name().send_keys("om")
        Your_Info_page.postal_code().send_keys("12345")
        Your_Info_page.continue_button().click()

        # now in Overview page
        overview = Overview_page(self.driver, wait)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        overview.finish_button().click()


        # now in cheakout compleate
        # complete page object
        Complete_page = checkoutComplete(self.driver, wait)
        URL = Complete_page.URL_get()
        # print(URL)
        if URL == 'https://www.saucedemo.com/checkout-complete.html':
            print("ho gya bhai")

        time.sleep(2)