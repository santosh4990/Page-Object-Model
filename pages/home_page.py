from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class HomePage(BasePage):
    FLIPKART_LOGO = (By.XPATH, "//img[@title='Flipkart']")
    SEARCH_BOX = (By.XPATH, "//input[@title='Search for Products, Brands and More' and @name='q']")
    
    def verify_flipkart_logo(self):
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FLIPKART_LOGO)).is_displayed()
    
    def search_for_product(self, product_name):
        search_box_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BOX))
        search_box_element.send_keys(product_name)
        search_box_element.send_keys(Keys.RETURN)

