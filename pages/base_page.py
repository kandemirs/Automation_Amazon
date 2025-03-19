from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click(self, by, locator):
        element = self.wait_for_element(by, locator)
        element.click()

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))


    def send_keys(self, by, locator, keys):
        element = self.wait_for_element(by, locator)
        element.send_keys(keys)


    def is_element_present(self, *locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

