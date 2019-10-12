import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
import time

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url=link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="success message don't disappeared after adding product to busket")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url=link)
    page.open()
    page.add_product_to_busket()
    page.should_not_be_success_message_after_time()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket_page()

class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    @pytest.fixture
    def setup(browser):
        page = BasePage(browser, url=self.link)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time.time()) + "@fakemail.org", "password")
        login_page.should_be_authorized_user()

    @pytest.mark.xfail(reason="guest see success message after adding product to busket")
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, url=self.link)
        page.open()
        page.add_product_to_busket()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, url=self.link)
        page.open()
        page.add_product_to_busket()