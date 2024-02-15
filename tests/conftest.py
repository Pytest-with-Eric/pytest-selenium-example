import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()

    # Use this line instead of the prev if you wish to download the ChromeDriver binary on the fly
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()