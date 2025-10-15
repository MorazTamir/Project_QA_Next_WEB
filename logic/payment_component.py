from selenium.webdriver.common.by import By
from infra.basepage import BasePage

class PaymentComponent(BasePage):



    NEXT_PAY_RADIOBUTTON = (By.XPATH, "//span[normalize-space(text())='nextpay']")
    PAY_IN_THREE_RADIOBUTTON  = (By.XPATH, "//span[normalize-space(text())='pay in 3']")
    CREDIT_DEBIT_CARD_RADIOBUTTON  = (By.XPATH, "//div[@id='WorldPayIframe-label' and normalize-space(text())='Credit / Debit Card']")
    PAYPAL_RADIOBUTTON  = (By.XPATH, "//div[@id='paypal-label' and normalize-space(text())='PayPal™']")
    GOOGLE_PAY_RADIOBUTTON  = (By.XPATH, "//div[@id='googlepay-label' and normalize-space(text())='Google Pay']")
    GIFTCARD_VOUCHER_RADIOBUTTON = (By.XPATH, "//div[@id='giftcard-label' and normalize-space(text())='Giftcard / eVoucher']")
    PAY_BY_BANK_RADIOBUTTON = (By.XPATH, "//div[@id='openbanking-label' and normalize-space(text())='Pay By Bank']")
    INPUT_CREDIT_CARD_NUMBER = (By.XPATH, "//input[@id='cardNumber']")
    INPUT_CREDIT_CARD_CARDHOLDERS_NAME = (By.XPATH, "//input[@id='cardholderName']")
    INPUT_CREDIT_CARD_EXPIRATION_DATE_MONTH = (By.XPATH, "//input[@id='expiryMonth']")
    INPUT_CREDIT_CARD_EXPIRATION_DATE_YEAR = (By.XPATH, "v//input[@id='expiryYear']")
    INPUT_CREDIT_CARD_SECURITY_CODE = (By.XPATH, "//input[@id='securityCode']")
    PAY_NOW = (By.XPATH, "//input[@id='submitButton']")


    def __init__(self, browse):
        super().__init__(browse)

    def next_pay_radiobutton(self):
        self.click_element(self.NEXT_PAY_RADIOBUTTON)

    def pay_in_three_radiobutton(self):
        self.click_element(self.PAY_IN_THREE_RADIOBUTTON)

    def credit_debit_card_radiobutton(self):
        self.click_element(self.CREDIT_DEBIT_CARD_RADIOBUTTON)

    def paypal_radiobutton(self):
        self.click_element(self.PAYPAL_RADIOBUTTON)

    def google_pay_radiobutton(self):
        self.click_element(self.GOOGLE_PAY_RADIOBUTTON)

    def giftcard_voucher_radiobutton(self):
        self.click_element(self.GIFTCARD_VOUCHER_RADIOBUTTON)

    def pay_by_bank_radiobutton(self):
        self.click_element(self.PAY_BY_BANK_RADIOBUTTON)

    def input_credit_card_number(self, number):
        self.type_input(self.INPUT_CREDIT_CARD_NUMBER, number)

    def input_credit_card_cardholders_name(self, name):
        self.type_input(self.INPUT_CREDIT_CARD_CARDHOLDERS_NAME, name)

    def input_credit_card_expiration_date_month(self, month):
        self.type_input(self.INPUT_CREDIT_CARD_EXPIRATION_DATE_MONTH, month)

    def input_credit_card_expiration_date_year(self, year):
        self.type_input(self.INPUT_CREDIT_CARD_EXPIRATION_DATE_YEAR, year)

    def input_credit_card_security_code(self, code):
        self.type_input(self.INPUT_CREDIT_CARD_SECURITY_CODE, code)

    def pay_now(self):
        self.click_element(self.PAY_NOW)