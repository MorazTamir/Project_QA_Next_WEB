from selenium.webdriver.common.by import By
from infra.basepage import BasePage


class MyAccountPage(BasePage):
    MY_ORDERS = (By.XPATH, "//a[text()='My Orders']")
    SAVED_CARDS = (By.XPATH, "//a[contains(@href, 'ManageSavedCards')]")
    NEXT_UNLIMITED = (By.XPATH, "//a[contains(@href, 'MyAccount/nextunlimited')]")
    SIGN_IN_DETAILS = (By.XPATH, "//a[contains(@href, 'UpdateSignInDetails')]")
    CONTACT_DETAILS = (By.XPATH, "//a[normalize-space(text())='Contact Details']")
    CONTINUE_SHOPPING = (By.XPATH, "//a[contains(@href, 'continue-shopping')]")
    SIGN_OUT = (By.XPATH, "//button[text()='SIGN OUT']")
    CHANGE_DETAILS = (By.XPATH, "//a[contains(@href, 'UpdateSignInDetails')]")
    CHANGE_BILLING_ADDRESS = (By.XPATH, "//a[normalize-space(text())='Change Billing Address']")

    def __init__(self, browser):
        super().__init__(browser)

    def open_my_orders(self):
        self.click_element(self.MY_ORDERS)

    def open_change_details(self):
        self.click_element(self.CHANGE_DETAILS)

    def open_change_billing_address(self):
        self.click_element(self.CHANGE_BILLING_ADDRESS)

    def open_saved_cards(self):
        self.click_element(self.SAVED_CARDS)
    def open_edit_sign_in(self):
        self.click_element(self.NEXT_UNLIMITED)

    def open_edit_billing(self):
        self.click_element(self.SIGN_IN_DETAILS)

    def open_contact_details(self):
        self.click_element(self.CONTINUE_SHOPPING )

    def click_continue_shopping(self):
        self.click_element(self.CONTINUE_SHOPPING)

    def sign_out(self):
        self.click_element(self.SIGN_OUT)

    def get_header_text(self):
        return self._driver.find_element(By.XPATH, self.MY_ORDERS).text

    def is_sign_out_button_visible(self):
        return self.is_element_displayed(self.SIGN_OUT)
