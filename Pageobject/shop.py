import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located

from Pageobject.cart import Cart
from Testscripts.conftest import browser
from utils.Browserutils import BrowserUtils


class Shop(BrowserUtils):

    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser
        self.product_names = (By.XPATH, "//div[@class='products']//div//h4") # name of the product
        self.product_increment = (By.XPATH, ".//div[@class='stepper-input']//a[2]") # increment plus button
        self.add_button = (By.XPATH, ".//div[@class='product-action']/button") # add to cart button
        self.item_price = (By.XPATH, ".//p[@class='product-price']")   # price per item in product card
        self.cart_button = (By.CSS_SELECTOR, "img[alt='Cart']") # cart button
        self.cart_total_price = (By.XPATH, "//div[@class='product-total']/p[2]")  # total inside cart
        self.search_text = (By.CSS_SELECTOR,"input[type='search']")
        self.search_product = (By.XPATH,"//div[@class='products']/div")
        self.cart_view = (By.CSS_SELECTOR,".cart-preview.active")
        self.checkout_button = (By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")

    def shop_element(self, product_name, quantity):
#Test case 1: add the item to the cart and verify the cart price
        products = self.driver.find_elements(*self.product_names)
        for item in products:

            if item.text.strip() == product_name:
                parent = item.find_element(By.XPATH, "./ancestor::div[@class='product']") # parent element for all the products

                # finding each products element based on the product name provided in JSON
                increment_btn = parent.find_element(*self.product_increment)
                add_btn = parent.find_element(*self.add_button)
                price_el = parent.find_element(*self.item_price)

                # click increment
                for _ in range(int(quantity) - 1):  # ensure quantity is int
                    increment_btn.click()

                # add to cart
                add_btn.click()

                # get unit price from product card
                prc_cart = int(price_el.text)
                cart_total = prc_cart * int(quantity)

                # open cart
                self.driver.find_element(*self.cart_button).click()

                # optional: verify cart total
                cart_price_el = self.driver.find_element(*self.cart_total_price)
                print("Product:", product_name)
                print("Quantity:", quantity)
                print("Unit price:", prc_cart)
                print("Calculated total:", cart_total)
                print("Cart displayed total:", cart_price_el.text)
                break

    def search(self,key):
# Test case 2 : search for an item and add to cart
        self.driver.find_element(*self.search_text).send_keys(key)
        time.sleep(3)
        search_item = self.driver.find_elements(*self.search_product)
        count = len(search_item)
        print("Search results:", count)
        if count ==0 :
            print("No products found")
        elif count >= 1:
            for item in search_item:
                item.find_element(By.XPATH,"div/button").click()
                break

    def checkout(self):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.checkout_button).click()
        checkout_page = Cart(self.driver)
        return checkout_page

    def get_title(self):
        return self.driver.title
























