from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    REJECT_BUTTON = (By.ID, "sp-cc-rejectall-link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_on_homepage(self):
        return "Amazon" in self.get_title()

    def search_for_product(self, product_name):
        self.send_keys(self.SEARCH_BOX[0], self.SEARCH_BOX[1], product_name)
        self.driver.find_element(*self.SEARCH_BOX).send_keys(Keys.RETURN)

    def reject_cookies(self):
        try:
            self.click(self.REJECT_BUTTON[0], self.REJECT_BUTTON[1])
            print("Çerezler reddedildi.")
        except:
            print("Reddet butonu bulunamadı.")

