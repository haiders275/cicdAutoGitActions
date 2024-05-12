import pytest
from selenium import webdriver


@pytest.fixture()
def setup_web():
    # driver = webdriver.Chrome()
    # return driver

    chromedriver_autoinstaller.install()

    chrome_options = webdriver.ChromeOptions()    
    options = [
        # Define window size here
        "--window-size=1200,1200",
        "--ignore-certificate-errors"
    ]

    for option in options:
        chrome_options.add_argument(option)

    
    driver = webdriver.Chrome(options = chrome_options)
    return driver
# executable_path="../chromeDriver/chromedriver.exe"
