import unittest
from infra.browser_wrapper import BrowserWrapperClass
from logic.login_page import LoginPage
from logic.my_account_component import MyAccountComponent
# from logic.wrong_login_page import WrongLoginPage

class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome', 'https://auth.next.co.uk/u/login')

    def test_login_successful(self):
        email = "fanustas@gmail.com"
        password = "can2020fanu"

        login_page = LoginPage(self.driver)

        login_page.close_cookies_popup()
        login_page.fill_email_user_input(email)
        login_page.fill_password_user_input(password)
        login_page.click_sign_in_button()

        my_account = MyAccountComponent(self.driver)
        self.assertEqual(my_account.get_header_text(), "My Orders")
        self.assertTrue(my_account.is_sign_out_button_visible())

    # def test_login_error(self):
    #     email = "fanustas@gmail.com"
    #     wrong_password = "1234567"
    #     login_page = LoginPage(self.driver)
    #
    #     login_page.close_cookies_popup()
    #     login_page.fill_email_user_input(email)
    #     login_page.fill_password_user_input(wrong_password)
    #     login_page.click_sign_in_button()
    #
    #     fail_login_page = WrongLoginPage(self.driver)
    #     self.assertEqual(fail_login_page.get_msg_text(), "Sorry, we have been unable to sign you in")

    def tearDown(self):
        self.driver.quit()
