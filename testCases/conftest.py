import pytest
from selenium import webdriver


@pytest.fixture()
def setup_web():
    driver = webdriver.Chrome("../chromeDriver/chromedriver.exe")
    return driver


# executable_path="../chromeDriver/chromedriver.exe"
