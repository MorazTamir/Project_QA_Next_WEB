from selenium.webdriver.common.by import By

class LoginPage:
    #base page - add
    #ELEMENTS
    EMAIL_USER_INOUT = '//input[@id="username"]'
    PASSWORD_USER_INPUT = '//input[@id="password"]'
    SIGN_IN_BUTTON = '//button[@type="submit"]' #2 the same

    def __init__(self, driver):
        self.driver = driver
        #Implementing locators
        self._email_user_input = self._driver.find_element(By.XPATH,self.EMAIL_USER_INOUT)
        self._password_user_input = self._driver.find_element(By.XPATH,self.PASSWORD_USER_INPUT)
        self._sign_in_button = self._driver.find_element(By.XPATH,self.SIGN_IN_BUTTON)

    #Implementation of functional actions
    def fill_email_user_input(self, email):
        self._email_user_input.sendKeys(email)

    def fill_password_user_input(self, password):
        self._password_user_input.sendKeys(password)

    def click_sign_in_button(self):
        self._sign_in_button.click()

    #Flow all the actions
    def login_flow(self, email, password):
        self.fill_email_user_input(email)
        self.fill_password_user_input(password)
        self.click_sign_in_button()