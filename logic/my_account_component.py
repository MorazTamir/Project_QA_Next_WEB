from selenium.webdriver.common.by import By
from infra.basepage import BasePage

class MyAccountComponent(BasePage):

    MY_ORDERS = (By.XPATH, "//a[text()='My Orders']")
    SAVED_CARDS = (By.XPATH, "//a[contains(@href, 'ManageSavedCards')]")
    NEXT_UNLIMITED = (By.XPATH, "//a[contains(@href, 'MyAccount/nextunlimited')]")
    SIGN_IN_DETAILS = (By.XPATH, "//a[contains(@href, 'UpdateSignInDetails')]")
    CONTACT_DETAILS = (By.XPATH, "//a[normalize-space(text())='Contact Details']")
    CONTINUE_SHOPPING = (By.XPATH, "//a[contains(@href, 'continue-shopping')]")
    SIGN_OUT = (By.XPATH, "//button[text()='SIGN OUT']")

    def __init__(self, browse):
        super().__init__(browse)

    def open_my_orders(self):
        self.click_element(self.MY_ORDERS)

    def open_saved_cards(self):
        self.click_element(self.SAVED_CARDS)

