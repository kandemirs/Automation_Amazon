from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class CartPage(BasePage):
    CART_ICON = (By.ID, "nav-cart")
    SUBTOTAL_LABEL = (By.ID, "sc-subtotal-label-buybox")
    DECREMENT_ICON = (By.CSS_SELECTOR, '[data-a-selector="decrement-icon"]')
    LOGO_LINK = (By.ID, "nav-logo-sprites")
    SUBTOTAL_LABEL1 = (By.ID, "sc-subtotal-label-activecart")

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_cart(self):
        self.click(self.CART_ICON[0], self.CART_ICON[1])

    def get_subtotal(self):
        subtotal_label = self.wait_for_element(*self.SUBTOTAL_LABEL)
        return subtotal_label.text

    def get_subtotal_items(self):
            subtotal_label = self.wait_for_element(*self.SUBTOTAL_LABEL1)
            return subtotal_label.text

    def remove_product(self):
        self.click(self.DECREMENT_ICON[0], self.DECREMENT_ICON[1])

    def go_to_homepage(self):
        self.click(self.LOGO_LINK[0], self.LOGO_LINK[1])
        print("Ana sayfaya geri gidildi.")

    def verify_cart_is_empty(self):
        subtotal_text = self.get_subtotal_items()
        if "0 ürün" in subtotal_text:
            return True
        return False