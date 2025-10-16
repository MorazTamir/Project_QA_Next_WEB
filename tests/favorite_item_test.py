import unittest
from infra.browser_wrapper import BrowserWrapperClass
from logic.item_page import ItemPage

class FavoriteItemTest(unittest.TestCase):
    def setUp(self):
        self.browser = BrowserWrapperClass()
        self.driver = self.browser.get_driver('Chrome', 'https://www.next.co.uk/style/su058723/n59402')

    def test_favorite_item(self):
        item_page = ItemPage(self.driver)
        item_page.close_cookies_popup()

        # Checking that the icon is empty
        initial_state = item_page.get_favorite_icon_state()
        if initial_state == "Remove from Favourites":
            item_page.click_favorite_btn()
            item_page.wait_for_favorite_state("Add to Favourites")
            initial_state = item_page.get_favorite_icon_state()

        assert initial_state == "Add to Favourites", "Expected empty (Add to Favourites) initially"

        # ACT
        item_page.click_favorite_btn()
        item_page.wait_for_favorite_state("Remove from Favourites")
        after_click_state = item_page.get_favorite_icon_state()
        print("After clicking favorite icon state:", after_click_state)
        assert after_click_state == "Remove from Favourites", "Expected filled (Remove from Favourites) after click"

    def tearDown(self):
        self.driver.quit()
