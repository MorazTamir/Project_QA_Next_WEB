from selenium.webdriver.common.by import By
from logic.login_page import LoginPage


class WrongLoginPage(LoginPage):
    MESSAGE_BOX = '//*[@id="messagebox"]'
    MSG_BOX_TITLE = '//*[@id="messagebox"]/div/div/span'

    def __init__(self, driver):
        super().__init__(driver)
        self._message_box = self._driver.find_element(By.XPATH, self.MESSAGE_BOX)
        self._msg_box_title = self._driver.find_element(By.XPATH, self.MSG_BOX_TITLE)

    def get_msg_text(self):
        return self._msg_box_title.text
