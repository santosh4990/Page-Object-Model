from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .base_page import BasePage  # Assuming BasePage is in the same directory


class ProductDetailPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")
    
    def add_to_cart(self):
        # Switching to the new tab (if applicable)
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        # Add to cart
        if EC.presence_of_element_located(self.ADD_TO_CART_BUTTON):
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ADD_TO_CART_BUTTON)).click()
