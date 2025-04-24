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
        wait = WebDriverWait(self.driver, 5)
        #object of Log_In_page
        Log_In_page = logInPage(self.driver, wait)

        # valid credencials
        user_name = "standard_user"
        pass_word = "secret_sauce"

        # home page actions
        Log_In_page.username_input_box().send_keys(user_name)
        Log_In_page.password_input_box().send_keys(pass_word)
        Homepage = Log_In_page.login_button()

        # Oject of homepage
        Homepage.button_backpack().click()
        Homepage.button_fleece_jacket().click()
        Cart_page = Homepage.shopping_cart_button()

        # now in cart
        Your_Info_page = Cart_page.checkout_button()

        # now in your information (cheakout)

        Your_Info_page.first_name().send_keys("hari")
        Your_Info_page.last_name().send_keys("om")
        Your_Info_page.postal_code().send_keys("12345")
        overview = Your_Info_page.continue_button()

        # now in Overview page
        self.scrollToEnd()
        Complete_page = overview.finish_button()


        # now in cheakout compleate
        # complete page object

        URL = Complete_page.URL_get()
        # print(URL)
        if URL == 'https://www.saucedemo.com/checkout-complete.html':
            print("ho gya bhai")

        time.sleep(2)