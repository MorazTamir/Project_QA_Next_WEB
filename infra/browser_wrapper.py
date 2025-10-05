from selenium import webdriver
from selenium.common import WebDriverException


class BrowserWrapperClass:

    # constructor - print that the tests start
    def __init__(self):
        print('Test Start!')
        self.driver = None
        # self.config =

    # The driver will receive a suitable browser
    def get_driver(self, browser, url):
        try:
            if browser == 'Chrome':
                self.driver = webdriver.Chrome()
            if browser == 'FireFox':
                self.driver = webdriver.Firefox()

            self.driver.get(url)
            self.driver.maximize_window()
            return self.driver
        except WebDriverException:
            #Driver Exception - occur during test automation
            print("WebDriver Exception: Error while opening browser")
