from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    BUY_NOW_BUTTON = (By.ID, "buy-now-button")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    SUCCESS_MESSAGE = (By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")


    def __init__(self, driver):
        super().__init__(driver)


    def is_on_product_page(self):
        try:
            self.wait_for_element(*self.BUY_NOW_BUTTON)
            return True
        except:
            return False

    def add_product_to_cart(self):
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if add_to_cart_buttons:
            add_to_cart_buttons[0].click()
            print("Ürün sepete eklendi.")
        else:
            print("Sepete ekle butonu bulunamadı.")

    def verify_product_added_to_cart(self):

        if self.is_element_present(*self.SUCCESS_MESSAGE):
            return True
        else:
            print("Sepete eklenme mesajı bulunamadı.")
            return False