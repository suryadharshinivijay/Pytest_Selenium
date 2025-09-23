from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.Browserutils import BrowserUtils


class Cart(BrowserUtils):
    def __init__(self,browser):
        super().__init__(browser)
        self.driver = browser
        self.promo_text = (By.CSS_SELECTOR, '.promoCode')
        self.promo_button = (By.CSS_SELECTOR, '.promoBtn')
        self.promo_button2 = (By.CSS_SELECTOR, '.promoInfo')
        self.order_button = (By.XPATH,"//button[normalize-space()='Place Order']")

    def cart_page(self,promo_code):
        self.driver.find_element(*self.promo_text).send_keys(promo_code)
        self.driver.find_element(*self.promo_button).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')) )
        promo_display = self.driver.find_element(*self.promo_button2).text
        assert (promo_display == "Invalid code ..!")

    def order_page(self):
        order_placed= self.driver.find_element(*self.order_button).click()

    def get_title(self):
        return self.driver.title



