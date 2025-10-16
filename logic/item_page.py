from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.basepage import BasePage
from logic.main_page import MainPage


class ItemPage(MainPage):
    # ELEMENTS
    ITEM_TITLE = '//*[@id="pdp-item-title"]/div/div[1]/div[1]/h1'
    ITEM_SELECT_COLOR = '//*[@id="pdp-description-form"]/div[1]/div[1]/div[1]/div[2]/div'
    ITEM_SELECT_SIZE = '//*[@id="pdp-description-form"]/div[1]/div[2]/div[2]/div'
    ADD_BUTTON = '//*[@id=":R9j69qlbedlqqd6:"]'
    FAVORITE_ICON_BUTTON = '//*[@id="pdp-item-form"]/div[1]/button[2]'
    COOKIES_REJECT_BTN = '//button[@id="onetrust-reject-all-handler"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._item_title = self._driver.find_element(By.XPATH, self.ITEM_TITLE)
        self._item_select_color = self._driver.find_element(By.XPATH, self.ITEM_SELECT_COLOR)
        self._item_select_size = self._driver.find_element(By.XPATH, self.ITEM_SELECT_SIZE)
        self._add_button = self._driver.find_element(By.XPATH, self.ADD_BUTTON)
        self._favorite_icon_btn = self._driver.find_element(By.XPATH, self.FAVORITE_ICON_BUTTON)

    def close_cookies_popup(self):
        try:
            cookies_button = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.COOKIES_REJECT_BTN))
            )
            cookies_button.click()
            print("✅ Cookies popup closed")
        except TimeoutException:
            print("No cookies popup found")

    def get_item_text(self):
        return self._item_title.text

    def choose_select_color(self, color="White"):
        self._item_select_color.click()

        color_options = WebDriverWait(self._driver, 5).until(
            lambda driver: driver.find_elements(By.XPATH, "//li[@role='option']")
        )

        for option in color_options:
            try:
                img = option.find_element(By.XPATH, ".//img")
                img_alt = img.get_attribute("alt").strip().lower()
            except:
                img_alt = ""
            text = option.text.strip().lower()

            if color.lower() in (text, img_alt):
                option.click()
                print(f"Color '{color}' selected")
                return

        raise Exception(f"Color '{color}' not found")

    def choose_alternative_size(self):
        self._item_select_size.click()

        size_options = WebDriverWait(self._driver, 5).until(
            lambda driver: driver.find_elements(By.XPATH, "//li[@role='option']")
        )

        if not size_options or len(size_options) < 2:
            raise Exception("No alternative size options found")

        for _ in range(len(size_options)):
            size_options = self._driver.find_elements(By.XPATH, "//li[@role='option']")
            for option in size_options[1:]:
                try:
                    option.click()
                    print(f"✅ Alternative size '{option.text}' selected")
                    return
                except:
                    continue

        raise Exception("No available alternative size could be selected")

    def click_add_btn(self):
        self._add_button.click()

    def click_favorite_btn(self):
        self._favorite_icon_btn.click()

    def get_favorite_icon_state(self):
        img = self._favorite_icon_btn.find_element(By.TAG_NAME, "img")
        return img.get_attribute("alt")

    # ----- WAIT METHODS -----
    def wait_for_favorite_state(self, expected_text, timeout=5):
        try:
            WebDriverWait(self._driver, timeout).until(
                lambda driver: self.get_favorite_icon_state() == expected_text
            )
        except TimeoutException:
            print(f"Timeout waiting for favorite state to be '{expected_text}'")