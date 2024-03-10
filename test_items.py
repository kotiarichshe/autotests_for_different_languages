from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_includes_a_add_to_cart_button(browser):
    browser.get(link)
    #time.sleep(30)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")

    
