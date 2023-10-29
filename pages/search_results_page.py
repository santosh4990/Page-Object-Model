from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .base_page import BasePage  # Assuming BasePage is in the same directory

class SearchResultsPage(BasePage):
    FIRST_ITEM = (By.XPATH, "//div[@class='_4rR01T']")

    def click_on_first_item(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIRST_ITEM)).click()


