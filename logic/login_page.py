from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.basepage import BasePage


class LoginPage(BasePage):
    # ELEMENTS (רק XPATH)
    EMAIL_USER_INPUT = '//input[@id="username"]'
    PASSWORD_USER_INPUT = '//input[@id="password"]'
    SIGN_IN_BUTTON = '//*[@id="loginWidget"]/main/section/div/div/div/form/div[2]/button'
    REGISTER_BUTTON = '//*[@id="registrationBtn"]'
    COOKIES_REJECT_BTN = '//button[@id="onetrust-reject-all-handler"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_USER_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_USER_INPUT)
        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)

    def fill_email_user_input(self, email):
        self._email_input.clear()
        self._email_input.send_keys(email)

    def fill_password_user_input(self, password):
        self._password_input.clear()
        self._password_input.send_keys(password)

    def click_sign_in_button(self):
        try:
            self._sign_in_button.click()
        except ElementClickInterceptedException:
            print("Take Screenshot")

    def close_cookies_popup(self):
        try:
            cookies_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.COOKIES_REJECT_BTN))
            )
            cookies_button.click()
            print("✅ Cookies popup closed")
        except TimeoutException:
            print("No cookies popup found")

    def full_login_flow(self, email, password):
        self.close_cookies_popup()
        self.fill_email_user_input(email)
        self.fill_password_user_input(password)
        self.click_sign_in_button()
