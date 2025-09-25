import json

import pytest
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from Pageobject import shop
from Pageobject.cart import Cart
from Pageobject.shop import Shop

test_data_path = '../data/test_functionaltest.json'
with open( test_data_path ) as f:
    test_data = json.load( f )
    test_list = test_data["data"]

test_data_path1 = '../data/search_funtionaltest.json'
with open(test_data_path1 ) as f:
    test_data = json.load( f )
    test_list1 = test_data["data"]

test_data_path2 = '../data/search_promocode.json'
with open(test_data_path1 ) as f:
    test_data = json.load( f )
    test_list2 = test_data["data"]

@pytest.fixture
def shop(browser):
    return Shop(browser)

@pytest.mark.smoke

# testcase1
# Open the browser
# Add items to the cart
# Open the cart
# Verify the cart total
@pytest.mark.parametrize("input_value", test_list)
def test_add(shop,input_value):

    shop.shop_element(input_value["product_name"],input_value["quantity"])
    print(shop.get_title())

# testcase2 -
# Open the browser
# Search for the element in search box
# click on "ADD to CART" button
@pytest.mark.parametrize("search_key", test_list1)
@pytest.mark.parametrize("promo_code", test_list2)
def test_search_apply_promo(shop,search_key,promo_code):

    shop.search(search_key["key"])

#test case 3:
# Enter the promo code in the checkout page
# assert promo code status in checkout page

    checkout_page= shop.checkout()
    checkout_page.cart_page(promo_code["code"])

#test case 4:
# Place the order from checkout page
# Verify user page navigates to choose country page
def test_order(shop,browser):

    checkout_page= shop.checkout()
    checkout_page.order_page()
    print(checkout_page.get_title())








