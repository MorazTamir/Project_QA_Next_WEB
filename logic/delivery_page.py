from selenium.webdriver.common.by import By
from basepage import basepage

class Delivery_page(basepage):

   CONTINUE_TO_PAYMENT = (By.XPATH,"//button[normalize-space(text())='Continue To Payment']")

   def __init__(self, browse):
       super().__init__(browse)

   def continue_to_payment(self):
       self.click_element(self.CONTINUE_TO_PAYMENT)