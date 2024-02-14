import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # Yield the WebDriver instance
    yield driver
    # Close the WebDriver instance
    driver.quit()


# def pytest_addoption(parser):
#     parser.addoption(
#         "--driver",
#         action="store",
#         default="Chrome",
#     )
#     parser.addoption(
#         "--driver-path",
#         action="store",
#         default="~/Downloads/chromedriver-mac-x64/chromedriver",
#     )
