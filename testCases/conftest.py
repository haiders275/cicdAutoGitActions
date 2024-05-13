import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

@pytest.fixture()
def setup_web(request):
    options=Options()
    options.add_argument("--headless")
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install(), options=options))
    request.cls.driver=driver

    yield
    driver.quit()

# @pytest.fixture()
# def setup_web():
    # driver = webdriver.Chrome()
    # return driver

#     chromedriver_autoinstaller.install()

#     chrome_options = webdriver.ChromeOptions()    
#     options = [
#         # Define window size here
#         "--window-size=1200,1200",
#         "--ignore-certificate-errors"
#     ]

#     for option in options:
#         chrome_options.add_argument(option)

    
#     driver = webdriver.Chrome(options = chrome_options)
#     return driver
# # executable_path="../chromeDriver/chromedriver.exe"
