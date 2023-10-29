from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, by_locator, timeout=20):
        """
        This method returns the element with the specified locator.
        It uses an explicit wait to ensure the element is visible before returning it.
        """
        element = WebDriverWait(self.driver, timeout).until(
            visibility_of_element_located(by_locator)
        )
        return element

    def click(self, by_locator):
        self.find_element(by_locator).click()

    def input_text(self, by_locator, text):
        self.find_element(by_locator).send_keys(text)
