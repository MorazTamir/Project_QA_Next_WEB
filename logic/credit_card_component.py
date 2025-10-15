from selenium.webdriver.common.by import By
from infra.basepage import BasePage

class CreditCardComponent(BasePage):
    CREDIT_CARD_NUMBER = (By.XPATH, "//a[@href='/my-orders']")
    CREDIT_CARD_OWNER = (By.XPATH, "//a[@href='/my-orders']")
    CREDIT_CARD_EXPIRATION_DATE = (By.XPATH, "//a[@href='/my-orders']")
    CREDIT_CARD_SECURITY_CODE = (By.XPATH, "//a[@href='/my-orders']")
    PAY_NOW = (By.XPATH, "//a[@href='/my-orders']")


