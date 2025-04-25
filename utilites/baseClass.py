import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class baseclass:

    def scrollToEnd(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_URL(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(locator))
        return self.driver.current_url

    def GettingLoggerNow(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logFile_01.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger


