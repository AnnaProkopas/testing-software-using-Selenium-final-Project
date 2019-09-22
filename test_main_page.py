from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com"

def test_add_to_cart(browser):
    page = MainPage(browser, url=link)
    page.open()
    #page.should_be_login_link()
    page.go_to_login_page()