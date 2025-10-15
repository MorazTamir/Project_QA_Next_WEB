from selenium.webdriver.common.by import By
from infra.basepage import basepage


class MyAccountPage(basepage):
    MY_ORDERS = (By.XPATH, "//a[text()='My Orders']")
    CHANGE_DETAILS = (By.XPATH, "//a[contains(@href, 'UpdateSignInDetails')]")
    CHANGE_BILLING_ADDRESS = (By.XPATH, "//a[normalize-space(text())='Change Billing Address']")

    # כאן אפשר להוסיף עוד locators לפי הצורך

    def __init__(self, browser):
        super().__init__(browser)

    def open_my_orders(self):
        self.click_element(self.MY_ORDERS)

    def open_change_details(self):
        self.click_element(self.CHANGE_DETAILS)

    def open_change_billing_address(self):
        self.click_element(self.CHANGE_BILLING_ADDRESS)
