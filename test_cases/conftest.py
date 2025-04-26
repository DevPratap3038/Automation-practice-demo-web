import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CO
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import re
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as CS
driver = None
import os

# === Path Setup ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.abspath(os.path.join(BASE_DIR, "../reports"))
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
HTML_REPORTS_DIR = os.path.join(REPORTS_DIR, "html_reports")

for folder in [SCREENSHOTS_DIR, HTML_REPORTS_DIR]:
    os.makedirs(folder, exist_ok=True)


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action='store', default='chrome'
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
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
        service = CS(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

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

# === Screenshot Capturing ===
def _capture_screenshot(file_name):
    global driver
    path = os.path.join(SCREENSHOTS_DIR, file_name)
    print(f"Trying to save screenshot to: {path}")
    print(f"Driver status: {driver}")  # Check if driver is None

    if driver is None:
        raise Exception("WebDriver is None. Cannot capture screenshot.")

    if not os.path.exists(SCREENSHOTS_DIR):
        os.makedirs(SCREENSHOTS_DIR)
        print(f"Created directory: {SCREENSHOTS_DIR}")

    success = driver.save_screenshot(path)
    if success:
        print(f"Screenshot saved successfully at {path}")
    else:
        print(f"Failed to save screenshot at {path}")

    return path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            raw_name = report.nodeid.replace("::", "_")
            safe_name = re.sub(r'[\\/:*?"<>|\[\]]', '_', raw_name)  # Replace invalid chars
            file_name = safe_name + ".png"
            _capture_screenshot(file_name)

            html = (
                f'<div><img src="../screenshots/{file_name}" alt="screenshot" '
                f'style="width:400px;height:300px;" '
                f'onclick="window.open(this.src)" align="right"/></div>'
            )
            extra.append(pytest_html.extras.html(html))
        report.extras = extra



# (use this to execute the code in cmd) pytest --html=reports/html_reports/report.html --self-contained-html --browser_name=chrome