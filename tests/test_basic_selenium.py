import pytest
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()


def test_title(driver):
    driver.get("https://www.python.org")
    assert driver.title == "Welcome to Python.org"
