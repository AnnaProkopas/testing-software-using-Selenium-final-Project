from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_FORM = (By.NAME, "login-username")
    LOGIN_PASS_FORM = (By.NAME, "login-password")

    REG_EMAIL_FORM = (By.NAME, "registration-email")
    REG_PASS1_FORM = (By.NAME, "registration-password1")
    REG_PASS2_FORM = (By.NAME, "registration-password2")

class ProductPageLocators():
    ADD_TO_BASCKET_BTN = (By.CSS_SELECTOR, "#add_to_basket_form .btn")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    MES_ABOUT_PUT_IN_BUSKET = (By.CLASS_NAME, "alertinner")
    PRODUCT_NAME_IN_BUSKET = (By.CSS_SELECTOR, ".alertinner strong")
    MINI_BASKET = (By.CLASS_NAME, "basket-mini")
    PRODUCT_COST = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")