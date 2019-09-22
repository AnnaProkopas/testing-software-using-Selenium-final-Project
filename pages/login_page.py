from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(self.browser.current_url)
        print(self.browser.current_url.find("login"))
        assert self.browser.current_url.find("login") >= 0, "Url is incorrect"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_FORM) and self.browser.find_element(*LoginPageLocators.LOGIN_PASS_FORM), "Form of login don't exist"
    
    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REG_EMAIL_FORM) and self.browser.find_element(*LoginPageLocators.REG_PASS1_FORM) and self.browser.find_element(*LoginPageLocators.REG_PASS2_FORM), "Form of register don't exist"