from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_FORM = (By.NAME, "login-username")
    LOGIN_PASS_FORM = (By.NAME, "login-password")

    REG_EMAIL_FORM = (By.NAME, "registration-email")
    REG_PASS1_FORM = (By.NAME, "registration-password1")
    REG_PASS2_FORM = (By.NAME, "registration-password2")