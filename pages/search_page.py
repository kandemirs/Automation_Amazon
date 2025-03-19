from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse, parse_qs

class SearchPage(BasePage):
    PAGINATION_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="2 sayfasına git"]')
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, 'button[aria-label="Sepete ekle"]')
    SEARCH_RESULT_TITLE = (By.CSS_SELECTOR, 'span.a-color-state.a-text-bold')
    PRODUCTS = (By.CSS_SELECTOR, 'div.s-main-slot div.s-result-item')

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_page(self, page_number):
        pagination_button = self.driver.find_element(*self.PAGINATION_BUTTON)
        pagination_button.click()

    def add_product_to_cart(self, index):
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if len(add_to_cart_buttons) > index:
            add_to_cart_buttons[index].click()
            print("Ürün sepete eklendi.")
        else:
            print("Sepete ekle butonu bulunamadı.")

    def verify_search_results(self, search_term):
        try:
            search_result_title = self.driver.find_element(*self.SEARCH_RESULT_TITLE).text
            return search_term.lower() in search_result_title.lower()
        except Exception as e:
            print(f"Arama sonucu başlığı bulunamadı: {e}")
            return False

    def scroll_to_product(self, index):
        add_to_cart_buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)

        if len(add_to_cart_buttons) > index:
            product_element = add_to_cart_buttons[index]
            actions = ActionChains(self.driver)
            actions.move_to_element(product_element).perform()
        else:
            print("3. ürün bulunamadı.")

    def verify_page_number_from_url(self, expected_page_number):

        current_url = self.driver.current_url
        parsed_url = urlparse(current_url)
        query_params = parse_qs(parsed_url.query)

        page_number = query_params.get('page', [None])[0]

        if page_number is None:
            return False

        return int(page_number) == expected_page_number


    def go_to_product(self, index):
        products = self.driver.find_elements(*self.PRODUCTS)
        if len(products) > index:
            product = products[index]
            product.click()

        else:
            print(f"{index + 1}. ürün bulunamadı.")