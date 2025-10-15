#Navigate between login and registration
import unittest
from infra.browser_wrapper import BrowserWrapperClass
from logic.login_page import LoginPage
from logic.register_page import RegisterPage

class NavigateLoginRegisterTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome', 'https://auth.next.co.uk/u/login')

    def test_navigate_login_signup(self):
        login_page = LoginPage(self.driver)
        login_page.close_cookies_popup()
        login_page.click_register_button()

        register_page = RegisterPage(self.driver)
        self.assertEqual(register_page.get_header_text(), "Quick Secure Sign Up")
        self.assertIn("Register", self.driver.current_url)

    def tearDown(self):
        self.driver.close()