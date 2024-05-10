import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def setup_web():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()
