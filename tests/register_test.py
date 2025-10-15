import unittest
from infra.browser_wrapper import BrowserWrapperClass
from logic.register_page import RegisterPage


class RegisterPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome', 'https://www.next.co.uk/secure/account/Register')

    def test_register_missing_field(self):
        first_name = 'SpongeBob'
        last_name = 'SquarePants'
        email = 'lipem40638@etenx.com'
        password = 'a1234567'
        date_of_birth = '101090'
        telephone_number = '0501234567'
        house_number = '5'
        postcode = '0'

        register_page = RegisterPage(self.driver)
        register_page.close_cookies_popup()
        register_page.choose_title()
        register_page.fill_first_name(first_name)
        register_page.fill_last_name(last_name)
        register_page.fill_email(email)
        register_page.fill_password(password)
        register_page.fill_date_birth(date_of_birth)
        register_page.fill_telephone(telephone_number)
        register_page.fill_house_number(house_number)
        register_page.fill_postcode(postcode)
        print("✅ All fields are complete")
        register_page.click_register_btn()

        # Assert
        self.assertEqual(register_page.get_error_text(), "Please enter a valid Postcode")

    def tearDown(self):
        self.driver.quit()
