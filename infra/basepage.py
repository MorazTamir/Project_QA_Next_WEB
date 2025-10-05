from pydoc import browse

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class basepage:
    def __init__(self, browse, timeout=10):
        self._browser = browse()
        self._timeout = timeout

    def get_url(self):
        return self._browser.url

    def get_page_title(self):
        return self._browser.title

    def refresh(self):
        self._browser.refresh()

    def find_singel_locator(self, locator):
        return WebDriverWait(self._browser, self._timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_all_locators(self, locator):
        return WebDriverWait(self._browser, self._timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        element = WebDriverWait(self._browser, self._timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type_input(self, locator, text, clear_first):
        element = self.find_singel_locator(locator)
        if not clear_first:
            element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_singel_locator(locator).text

    def is_element_displayed(self, locator):
        try:
            return self.find_singel_locator(locator).is_displayed()
        except TimeoutException:
            return False
