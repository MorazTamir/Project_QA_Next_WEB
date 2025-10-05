import unittest

from infra.browser_wrapper import BrowserWrapperClass
from logic.login_page import LoginPage


class LoginPageTest(unittest.TestCase):
    URL_LOGIN = 'https://auth.next.us/u/login?state=hKFo2SBJTnlOcFlITHc5VWU5Zlg4am05OFV3V1NnYnBxRWY1VqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIDhpMVI4MWVzZFZ5Rk9vaUxoYm9PMlh4TnFjUDgzc3llo2NpZNkgdjhETVEyVnN2THI3OTloVXdDMUZUdzE3NTJXdFFzMjQ&ext-country=US&ext-lang=en&QParam='

    def setUp(self):
        #Run every time before test
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome','URL_LOGIN')

    def test_login_suc(self):
        #Arrange
        email = 'lipem40638@etenx.com'
        password = 'Test1234'
        login_page = LoginPage(self.driver)

        #Steps
        login_page.fill_email_user_input(email)
        login_page.fill_password_user_input(password)
        #Act:
        login_page.click_sign_in_button()
        #Assert - New page - login succesful -POM new page: https://account.next.co.il/he/MyAccount/OrderTracking
        #we can assert url, or title - My orders