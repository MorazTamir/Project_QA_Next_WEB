from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.basepage import BasePage

class MyAccountPage(BasePage):
    # ELEMENTS
    MY_ORDERS = "//a[text()='My Orders']"
    SAVED_CARDS = "//a[contains(@href, 'ManageSavedCards')]"
    NEXT_UNLIMITED = "//a[contains(@href, 'MyAccount/nextunlimited')]"
    SIGN_IN_DETAILS = "//a[contains(@href, 'UpdateSignInDetails')]"
    CONTACT_DETAILS = "//a[normalize-space(text())='Contact Details']"
    CONTINUE_SHOPPING = "//a[contains(@href, 'continue-shopping')]"
    SIGN_OUT = "//button[text()='SIGN OUT']"
    CHANGE_DETAILS = "//a[contains(@href, 'UpdateSignInDetails')]"
    CHANGE_BILLING_ADDRESS = "//a[normalize-space(text())='Change Billing Address']"

    def __init__(self, driver, timeout=10):
        super().__init__(driver)
        wait = WebDriverWait(driver, timeout)

        self._my_orders = wait.until(EC.presence_of_element_located((By.XPATH, self.MY_ORDERS)))
        self._saved_cards = wait.until(EC.presence_of_element_located((By.XPATH, self.SAVED_CARDS)))
        self._next_unlimited = wait.until(EC.presence_of_element_located((By.XPATH, self.NEXT_UNLIMITED)))
        self._sign_in_details = wait.until(EC.presence_of_element_located((By.XPATH, self.SIGN_IN_DETAILS)))
        self._contact_details = wait.until(EC.presence_of_element_located((By.XPATH, self.CONTACT_DETAILS)))
        self._continue_shopping = wait.until(EC.presence_of_element_located((By.XPATH, self.CONTINUE_SHOPPING)))
        self._sign_out = wait.until(EC.presence_of_element_located((By.XPATH, self.SIGN_OUT)))
        self._change_details = wait.until(EC.presence_of_element_located((By.XPATH, self.CHANGE_DETAILS)))
        self._change_billing_address = wait.until(EC.presence_of_element_located((By.XPATH, self.CHANGE_BILLING_ADDRESS)))


    # METHODS
    def open_my_orders(self):
        self._my_orders.click()

    def open_saved_cards(self):
        self._saved_cards.click()

    def open_next_unlimited(self):
        self._next_unlimited.click()

    def open_sign_in_details(self):
        self._sign_in_details.click()

    def open_contact_details(self):
        self._contact_details.click()

    def click_continue_shopping(self):
        self._continue_shopping.click()

    def open_change_details(self):
        self._change_details.click()

    def open_change_billing_address(self):
        self._change_billing_address.click()

    def sign_out(self):
        self._sign_out.click()

    def get_my_orders_text(self):
        return self._my_orders.text

    def is_sign_out_button_visible(self):
        return self._sign_out.is_displayed()
