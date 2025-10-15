from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.basepage import BasePage


class RegisterPage(BasePage):
    # ELEMENTS
    TITLE_SELECT = '//*[@id="Title"]'
    FIRST_NAME_INPUT = '//*[@id="FirstName"]'
    LAST_NAME_INPUT = '//*[@id="LastName"]'
    EMAIL_INPUT = '//*[@id="Email"]'
    PASSWORD_INPUT = '//*[@id="Password"]'
    DATE_BIRTH_INPUT = '//*[@id="DobDate"]'
    TELEPHONE_INPUT = '//*[@id="PhoneNumber"]'
    HOUSE_NUMBER_INPUT = '//*[@id="HouseNumberOrName"]'
    POSTCODE_INPUT = '//*[@id="Postcode"]'
    REGISTER_BUTTON = '//*[@id="SignupButton"]'
    COOKIES_REJECT_BTN = '//button[@id="onetrust-reject-all-handler"]'
    POSTCODE_ERROR = '//*[@id="Postcode-error"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._title_select = self._driver.find_element(By.XPATH, self.TITLE_SELECT)
        self._first_name_input = self._driver.find_element(By.XPATH, self.FIRST_NAME_INPUT)
        self._last_name_input = self._driver.find_element(By.XPATH, self.LAST_NAME_INPUT)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._date_birth_input = self._driver.find_element(By.XPATH, self.DATE_BIRTH_INPUT)
        self._telephone_input = self._driver.find_element(By.XPATH, self.TELEPHONE_INPUT)
        self._house_number_input = self._driver.find_element(By.XPATH, self.HOUSE_NUMBER_INPUT)
        self._postcode_input = self._driver.find_element(By.XPATH, self.POSTCODE_INPUT)
        self._register_btn = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def choose_title(self):
        select = Select(self._title_select)
        select.select_by_visible_text("Mr")

    def fill_first_name(self, name):
        self._first_name_input.send_keys(name)

    def fill_last_name(self, last_name):
        self._last_name_input.send_keys(last_name)

    def fill_email(self, email):
        self._email_input.send_keys(email)

    def fill_password(self, password):
        self._password_input.send_keys(password)

    def fill_date_birth(self, date_birth):
        self._date_birth_input.send_keys(date_birth)

    def fill_telephone(self, telephone):
        self._telephone_input.send_keys(telephone)

    def fill_house_number(self, house_number):
        self._house_number_input.send_keys(house_number)

    def fill_postcode(self, postcode):
        self._postcode_input.send_keys(postcode)

    def click_register_btn(self):
        self._register_btn.click()

    def get_error_text(self):
        return self._driver.find_element(By.XPATH, self.POSTCODE_ERROR).text

    def close_cookies_popup(self):
        try:
            cookies_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.COOKIES_REJECT_BTN))
            )
            cookies_button.click()
            print("✅ Cookies popup closed")
        except TimeoutException:
            print("No cookies popup found")

    def full_register(self, first_name, last_name, email, password, date_birth, telephone, house_number, postcode):
        self.close_cookies_popup()
        self.choose_title()
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_email(email)
        self.fill_password(password)
        self.fill_date_birth(date_birth)
        self.fill_telephone(telephone)
        self.fill_house_number(house_number)
        self.fill_postcode(postcode)
        self.click_register_btn()
