from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    browser: webdriver
    url: str
    def __init__(self, browser: webdriver, url: str, timeout:int=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    
    def open(self):
        self.browser.get(self.url)