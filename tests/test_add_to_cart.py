import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import time

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # Go to https://www.amazon.com.tr/
        self.driver.get("https://www.amazon.com.tr/")

    def test_add_to_cart(self):
        home_page = HomePage(self.driver)
        time.sleep(1)

        # Verify that you are on the home page
        self.assertTrue(home_page.is_on_homepage(), "This is not homepage!")

        home_page.reject_cookies()

        # Type 'samsung' in the search field at the top of the screen and perform search.
        home_page.search_for_product("Samsung")
        search_page = SearchPage(self.driver)

        # Verify that there are results for Samsung on the page that appears.
        self.assertTrue(search_page.verify_search_results("Samsung"), "Sayfada ilgili samsung araması yapılamadı.")

        # Click on the 2nd page from the search results and verify that the 2nd page is
        # currently displayed on the page that opens.
        search_page.go_to_page(2)
        time.sleep(3)
        self.assertTrue(search_page.verify_page_number_from_url(2), "Sayfa numarası doğrulanamadı, 2. sayfa açılmadı.")

        # Go to the 3rd Product page from the top
        search_page.scroll_to_product(2)
        time.sleep(8)
        search_page.go_to_product(4)
        time.sleep(6)

        # Verify that you are on the product page
        product_page = ProductPage(self.driver)
        self.assertTrue(product_page.is_on_product_page(), "Ürün syfası görüntülenemedi.")

        # Add the product to the cart
        product_page.add_product_to_cart()
        time.sleep(3)

        # Verify that the product has been added to the cart
        self.assertTrue(product_page.verify_product_added_to_cart(), "Ürün sepete eklenmedi.")
        time.sleep(3)

        # Go to the cart page
        cart_page = CartPage(self.driver)
        cart_page.go_to_cart()
        time.sleep(3)

        # Verify that you are on the cart page and that the correct product has been added to
        # the cart
        subtotal_text = cart_page.get_subtotal()
        print(f" {subtotal_text}")
        time.sleep(3)


        # Delete the product from the cart and verify that it has been deleted
        cart_page.remove_product()
        time.sleep(4)
        self.assertTrue(cart_page.verify_cart_is_empty(), "Sepet boş değil. Ürün silinemedi.")

        #Return to the home page and verify that it is on the home page
        cart_page.go_to_homepage()
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()