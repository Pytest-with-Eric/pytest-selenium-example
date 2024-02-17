"""
SearchPage class to interact with the search page on DuckDuckGo
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def search(self, search_term):
        search_box = self.driver.find_element(By.ID, value="searchbox_input")
        search_box.send_keys(search_term + Keys.RETURN)
