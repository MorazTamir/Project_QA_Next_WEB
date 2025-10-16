import unittest
from infra.browser_wrapper import BrowserWrapperClass
from logic.item_page import ItemPage


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome', 'https://www.next.co.uk/style/su058723/n59402')

    def test_add_item(self):
        color = 'White'
        size_index1 = 2
        size_index2 = 4

        item_page = ItemPage(self.driver)
        item_page.close_cookies_popup()
        initial_count = item_page.get_cart_item_count()
        print(f"Initial cart count: {initial_count}")

        item_page.choose_select_color(color)
        self.driver.implicitly_wait(5)
        item_page.choose_alternative_size()
        self.driver.implicitly_wait(5)

        item_page.click_add_btn()
        updated_count = item_page.get_cart_item_count()
        print(f"Updated cart count: {updated_count}")

        assert updated_count == initial_count + 1, f"Expected {initial_count + 1}, got {updated_count}"

    def tearDown(self):
        self.driver.quit()