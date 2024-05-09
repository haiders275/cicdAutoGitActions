from selenium.webdriver.common.by import By
from utilities.customlogger import LogGen


class GooglePage:
    search_box_locator = 'q'

    log = LogGen.loggen()

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.google.com/')

    def get_title(self):
        Title = self.driver.title
        print(Title)
        if Title == "Google":
            print("Test Passed.")
            self.log.info("Test Passed.")

        else:
            print("Title not verified.")
            self.log.info("Title not verified.")

    def is_search_box_present(self):
        searchField = (self.driver.find_element(By.NAME, self.search_box_locator))
        if searchField.is_displayed():
            print("Test Passed Search field.")
            self.log.info("Search Field displayed. Test Passed.")

        else:
            print("Test Failed Search field.")
            self.log.info("Search Field not displayed. Test Failed.")
