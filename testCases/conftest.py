import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def setup_web():
    driver=webdriver.Chrome()
    return driver
    driver.quit()
