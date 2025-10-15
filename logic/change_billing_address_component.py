from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from logic.my_account_page import MyAccountPage

class ChangeBillingAddressComponent(MyAccountPage):
    INPUT_HOUSE_NUMBER_OR_NAME = (By.XPATH, "//input[@id='HouseNumberOrName']")
    INPUT_POSTCODE = (By.XPATH, "//input[@id='Postcode']")
    CLICK_FIND_ADDRESS_BUTTON = (By.XPATH, "//input[@name='FindAddress']")
    DROPDOWN_SELECT_ADDRESS = (By.XPATH, "//select[@id='AddressListSelection']")

    def enter_house_number_or_name(self, name):
        self.type_input(self.INPUT_HOUSE_NUMBER_OR_NAME, name)

    def enter_postcode(self, code):
        self.type_input(self.INPUT_POSTCODE, code)

    def click_find_address(self):
        self.click_element(self.CLICK_FIND_ADDRESS_BUTTON)

    def select_address_from_dropdown(self, value):
        dropdown = Select(self.find_single_locator(self.DROPDOWN_SELECT_ADDRESS))
        dropdown.select_by_visible_text(value)

    # אם יש כפתור Confirm, יש להוסיף כאן פונקציה
    def confirm_address_selection(self):
        pass  # implement if needed

    # אם יש הודעת הצלחה, פונקציה לקבלתה
    def get_success_message(self):
        pass  # implement if needed
