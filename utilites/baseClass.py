import pytest

@pytest.mark.usefixtures("setup")
class baseclass:
    def scrollToEnd(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


