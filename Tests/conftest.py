import pytest
from Utility import utility_file
from selenium import webdriver

@pytest.fixture()

def setup_and_teardown(request):
    browser = utility_file.get_config("basic info","browser")
    driver = None
    if browser.__eq__("Chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("Firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("Edge"):
        driver = webdriver.Edge()
    else:
        print("Provide Correct browser name")
    
    driver.maximize_window()
    url = utility_file.get_config("basic info","url")
    driver.get(url)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.quit()