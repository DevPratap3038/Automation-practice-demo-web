import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilites.baseClass import baseclass
from pages_objects.log_in_page import logInPage
from pages_objects.home_page import HomePage
from pages_objects.cart_page import Cart
from pages_objects.checkout_page_your_info import your_info
from pages_objects.checkout_page_overview import Overview_page
from pages_objects.cheakout_Complete import checkoutComplete



class Test_class_02(baseclass):
    def test_def_02(self, get_credintials):
        wait = WebDriverWait(self.driver, 5)
        Log_In_page = logInPage(self.driver, wait)

        # valid credencials
        # username = get_credintials[username]
        # password = get_credintials[username]

        # home page actions
        log = self.GettingLoggerNow()
        log.info("Entring the Username" + get_credintials["username"] )
        Log_In_page.username_input_box().send_keys(get_credintials["username"])
        log.info("Entring the Password" + get_credintials["password"])
        Log_In_page.password_input_box().send_keys(get_credintials["password"])
        log.info("Clicking the login button")
        Log_In_page.login_button()
        url = self.get_URL((By.XPATH, "//span[@class='title']"))
        log.info("Gitting current Url  = " + url)
        assert url == "https://www.saucedemo.com/inventory.html"
    #     ,("locked_out_user","secret_sauce"),("visual_user","secret_sauce"),("error_user","secret_sauce")
        self.driver.back()
        self.driver.refresh()

    @pytest.fixture(params=[{"username":"standard_user","password":"secret_sauce"}, {"username":"problem_user", "password":"secret_sauce"}, {"username": "performance_glitch_user", "password":"secret_sauce"}])
    def get_credintials(self, request):
        return request.param