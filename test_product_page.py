import pytest
from pages.product_page import ProductPage
import time
"""
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
                
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, url=link)
    page.open()
    page.add_product_to_busket()
"""
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.xfail(reason="guest see success message after adding product to busket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=link)
    page.open()
    print(" ---- >>> <<< ---- ")
    page.add_product_to_busket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="guest don't see success message without adding product to busket")
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url=link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="success message don't disappeared after adding product to busket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url=link)
    page.open()
    page.add_product_to_busket()
    page.should_not_be_success_message_after_time()