from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._timeout = timeout

    def get_url(self):
        return self._driver.current_url

    def get_page_title(self):
        return self._driver.title

    def refresh(self):
        self._driver.refresh()

    def find_single_locator(self, locator):
        return WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_all_locators(self, locator):
        return WebDriverWait(self._driver, self._timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        element = WebDriverWait(self._driver, self._timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_input(self, locator, text, clear_first=True):
        element = self.find_single_locator(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_single_locator(locator).text

    def is_element_displayed(self, locator):
        try:
            return self.find_single_locator(locator).is_displayed()
        except TimeoutException:
            return False
