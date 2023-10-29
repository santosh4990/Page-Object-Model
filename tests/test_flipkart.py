import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Keep the fixture the same
@pytest.fixture(scope="function")
def setup_and_teardown():
    chrome_driver_path = ChromeDriverManager().install()
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_flipkart_shopping(setup_and_teardown):
    driver = setup_and_teardown
    base_page = BasePage(driver)
    home_page = HomePage(driver)
    search_page = SearchResultsPage(driver)
    product_page = ProductDetailPage(driver)

    # Open the Flipkart URL
    base_page.open_url("https://www.flipkart.com/")
    
    # Verify that the Flipkart logo is present
    home_page.verify_flipkart_logo()

    # Search for "Macbook air m2" and hit Enter
    home_page.search_for_product("Macbook air m2")

    # Click on the first displayed item
    search_page.click_on_first_item()

    # Switch to new tab if necessary and add to cart
    product_page.add_to_cart()

if __name__ == "__main__":
    pytest.main()
