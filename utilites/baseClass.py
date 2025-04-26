import inspect
import logging
import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from test_cases.conftest import LOGS_DIR
from test_cases.conftest import REPORTS_DIR


@pytest.mark.usefixtures("setup")
class baseclass:

    def scrollToEnd(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_URL(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(locator))
        return self.driver.current_url

    # LOGS_DIR = os.path.join(REPORTS_DIR, "logs")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOGS_DIR = os.path.join(BASE_DIR, "../reports", "logs")
    os.makedirs(LOGS_DIR, exist_ok=True)

    def GettingLoggerNow(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler(os.path.join(baseclass.LOGS_DIR, "logFile_01.log"))
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        if not logger.handlers:
            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)

        return logger


