from selenium import webdriver
from selenium.common import WebDriverException


class BrowserWrapperClass:

    def __init__(self):
        print('Test Start!')
        self.driver = None
        # self.config =

    def get_driver(self, browser, url):
        try:
            if browser == 'Chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'FireFox':
                self.driver = webdriver.Firefox()

            self.driver.get(url)
            self.driver.maximize_window()
            return self.driver
        except WebDriverException:
            print("WebDriver Exception: Error while opening browser")

    def close_browser(self):
        print("Test finish")
        if self.driver:
            self.driver.quit()
