from selenium.webdriver.common.by import By
from infra.basepage import BasePage
from my_account_page import MyAccountPage

class SignInDetailsComponent(BasePage, MyAccountPage):



    INPUT_EMAIL_ADDRESS = (By.XPATH, "//input[@id='EmailAddress']")
    INPUT_NEW_PASSWORD = (By.XPATH, "//input[@id='Password']")
    REQUEST_A_CALL_BACK = (By.XPATH, "//a[normalize-space(text())='Request a Call Back']")

    def __init__(self, browse):
        super().__init__(browse)

    def input_email_address(self, email):
        self.type_input(self.INPUT_EMAIL_ADDRESS, email)

    def input_new_password(self, password):
        self.type_input(self.INPUT_NEW_PASSWORD, password)

    def request_a_call_back(self):
        self.click_element(self.REQUEST_A_CALL_BACK )