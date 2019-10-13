from .base_page import BasePage
from .locators import ProductPageLocators
import math
import time 


class ProductPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_time(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "Product name not found"

    def should_be_messange(self):
        assert self.is_element_present(*ProductPageLocators.MES_ABOUT_PUT_IN_BUSKET), \
            "Messange about put in busket not found"

    def should_be_add_product_to_busket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASCKET_BTN), \
            "Button to add product to busket not found"

    def should_be_product_cost(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_COST), \
            "The product cost not found "

    def should_be_this_product_in_busket(self):
        self.should_be_product_name()
        self.should_be_messange()
        self.should_be_product_cost()
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
            self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BUSKET).text, \
            "The product is in the message and this product does not match"
        assert  self.browser.find_element(*ProductPageLocators.MINI_BASKET).text.find( \
            self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text), \
            "The product cost and the value of the basket do not match"

    def add_product_to_busket(self):
        self.should_be_add_product_to_busket_btn()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASCKET_BTN).click()
        self.should_be_this_product_in_busket()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
    
    def add_product_to_busket_with_code(self):
        self.should_be_add_product_to_busket_btn()
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASCKET_BTN).click()
        self.solve_quiz_and_get_code()
        self.should_be_this_product_in_busket()