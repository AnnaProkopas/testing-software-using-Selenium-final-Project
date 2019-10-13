from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    
    def should_be_empty_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "exist elements in basket"
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text