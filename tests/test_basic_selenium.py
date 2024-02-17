from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_title(chrome_browser):
    """
    Test the title of the Python.org website
    """
    chrome_browser.get("https://www.python.org")
    assert chrome_browser.title == "Welcome to Python.org"


def test_search(chrome_browser):
    """
    Test the search functionality of the DuckDuckGo website
    """
    url = "https://duckduckgo.com/"
    search_term = "Pytest with Eric"
    # Navigate to the Google home page.
    chrome_browser.get(url)

    # Find the search box using its name attribute value.
    search_box = chrome_browser.find_element(By.ID, value="searchbox_input")

    # Enter a search query and submit.
    search_box.send_keys(search_term + Keys.RETURN)

    # Assert that the title contains the search term.
    assert search_term in chrome_browser.title


def test_login_functionality(chrome_browser):
    """
    Test the login functionality of the Practice Test Automation website
    """
    url = "https://practicetestautomation.com/practice-test-login/"

    # Navigate to the login page
    chrome_browser.get(url)

    # Find and fill the username and password fields
    chrome_browser.find_element(By.ID, "username").send_keys("student")
    chrome_browser.find_element(By.ID, "password").send_keys("Password123")

    # Find and click the login button
    chrome_browser.find_element(By.ID, "submit").click()

    # Verify that the login was successful by checking the presence of a logout button
    # Option 1: Locate by class name (if unique and reliable)
    try:
        logout_button = chrome_browser.find_element(
            By.CLASS_NAME, "wp-block-button__link"
        )
        assert logout_button.is_displayed(), "Logout button is not displayed."
    except NoSuchElementException:
        assert False, "Logout button does not exist."

    # Option 2: Locate by link text (if the text is unique and reliable)
    try:
        logout_button = chrome_browser.find_element(By.LINK_TEXT, "Log out")
        assert logout_button.is_displayed(), "Logout button is not displayed."
    except NoSuchElementException:
        assert False, "Logout button does not exist."


def test_pytest_selenium_plugin_example(selenium):
    """
    Test the title and description of the Pytest with Eric website using the pytest-selenium plugin
    """
    selenium.implicitly_wait(10)
    selenium.get("https://pytest-with-eric.com")

    # Assert Web page title
    assert selenium.title == "Pytest With Eric"

    # Get Description
    # Locate the meta tag by its name attribute
    meta_description = selenium.find_element(By.XPATH, "//meta[@name='description']")

    # Retrieve the content attribute of the meta tag
    content_value = meta_description.get_attribute("content")

    #  Assert the content attribute's value
    expected_content = "Learn to write production level Python Unit Tests with Pytest"
    assert content_value == expected_content


# TODO - Show Tests with Parametrization for different browsers

# TODO - Show Tests with the Page Object Model
