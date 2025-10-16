
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from infra.basepage import BasePage
from selenium.webdriver import ActionChains

class MainPage(BasePage):


    HOVER_OVER_WOMEN_HEADER = (By.XPATH, "//div[normalize-space(text())='women']")
    HOVER_OVER_MEN_HEADER = (By.XPATH, "//div[normalize-space(text())='men']")
    HOVER_OVER_BOYS_HEADER = (By.XPATH, "//div[normalize-space(text())='boys']")
    HOVER_OVER_GIRLS_HEADER = (By.XPATH, "//div[normalize-space(text())='girls']")
    HOVER_OVER_HOME_HEADER = (By.XPATH, "//div[normalize-space(text())='home']")
    HOVER_OVER_BABY_HEADER = (By.XPATH, "//div[normalize-space(text())='baby']")
    HOVER_OVER_CHRISTMAS_HEADER = (By.XPATH, "//div[normalize-space(text())='christmas']")
    HOVER_OVER_FURNITURE_HEADER = (By.XPATH, "//div[normalize-space(text())='furniture']")
    HOVER_OVER_BRANDS_HEADER = (By.XPATH, "//div[normalize-space(text())='brands']")
    HOVER_OVER_BEAUTY_HEADER = (By.XPATH, "//div[normalize-space(text())='beauty']")
    HOVER_OVER_GIFTS_FLOWERS_HEADER = (By.XPATH, "//div[normalize-space(text())='gifts & flowers']")
    HOVER_OVER_SPORTS_HEADER = (By.XPATH, "//div[normalize-space(text())='sports']")
    HOVER_OVER_CLEARANCE_HEADER = (By.XPATH, "//div[normalize-space(text())='clearance']")
    CLICK_FAVORITE_ICON = (By.XPATH, "//img[@alt='Favourites icon']")
    CLICK_MY_ACCOUNT_ICON = (By.XPATH, "//img[contains(@src,'next_my-account_desktop.svg')]")
    CLICK_SHOPPING_BUG_ICON = (By.XPATH, '//*[@id="platform_modernisation_header"]/header/div[1]/nav/div[3]/span/div/div[2]/a')
    CLICK_CHECKOUT_ICON = (By.XPATH, "//a[normalize-space(text())='CHECKOUT']")


    def __init__(self, driver):
        super().__init__(driver)

    def hover_over_women_header(self):
        element = self.find_single_locator(self.HOVER_OVER_WOMEN_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_men_header(self):
        element = self.find_single_locator(self.HOVER_OVER_MEN_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_boys_header(self):
        element = self.find_single_locator(self.HOVER_OVER_BOYS_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_girls_header(self):
        element = self.find_single_locator(self.HOVER_OVER_GIRLS_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_home_header(self):
        element = self.find_single_locator(self.HOVER_OVER_HOME_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_baby_header(self):
        element = self.find_single_locator(self.HOVER_OVER_BABY_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_christmas_header(self):
        element = self.find_single_locator(self.HOVER_OVER_CHRISTMAS_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_furniture_header(self):
        element = self.find_single_locator(self.HOVER_OVER_FURNITURE_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_brands_header(self):
        element = self.find_single_locator(self.HOVER_OVER_BRANDS_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_beauty_header(self):
        element = self.find_single_locator(self.HOVER_OVER_BEAUTY_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_gifts_flowers_header(self):
        element = self.find_single_locator(self.HOVER_OVER_GIFTS_FLOWERS_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_sports_header(self):
        element = self.find_single_locator(self.HOVER_OVER_SPORTS_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def hover_over_clearance_header(self):
        element = self.find_single_locator(self.HOVER_OVER_CLEARANCE_HEADER)
        actions = ActionChains(self._driver)
        actions.move_to_element(element).perform()

    def click_favourite_icon(self):
        self.click_element(self.CLICK_FAVORITE_ICON)

    def click_my_account_icon(self):
        self.click_element(self.CLICK_MY_ACCOUNT_ICON)

    def click_shopping_bug_icon(self):
        self.click_element(self.CLICK_SHOPPING_BUG_ICON )

    def click_checkout_icon(self):
        self.click_element(self.CLICK_CHECKOUT_ICON)

    def get_cart_item_count(self, timeout=5):
        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located(self.CLICK_SHOPPING_BUG_ICON)
            )
            return int(element.text)
        except (ValueError, TimeoutException):
            return 0