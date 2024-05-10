import pytest
from selenium import webdriver


@pytest.fixture()
def setup_web():
    driver = webdriver.Chrome()
    yield driver
