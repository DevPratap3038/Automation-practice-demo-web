import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from webdriver_manager.firefox import GeckoDriverManager



def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action='store', default='chrome'
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = CO()
        chrome_options.add_argument("--start-maximized")
        prefs = {
            "credentials_enable_service": False,  # Disable Chrome's password manager
            "profile.password_manager_enabled": False  # Disable saving passwords prompt
        }

        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-features=PasswordCheck,PasswordManagerRedesign")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-features=PasswordManagerOnboarding")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)

    elif browser_name == "ms_edge":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--disable-popup-blocking")
        driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(),options= options)


    elif browser_name == "firefox":
        driver =  driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


    driver.get("https://www.saucedemo.com/")
    request.cls.driver = driver
    yield
    driver.close()

