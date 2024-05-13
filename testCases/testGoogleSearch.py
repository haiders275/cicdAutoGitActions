import allure
import pytest
from pageObjects.webApp_Page import GooglePage
from utilities.customlogger import LogGen


class TestGoogleSearchField:
    log = LogGen.loggen()
    
    # @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_field_presence(self, setup_web):
        self.driver = setup_web
        self.driver.maximize_window()
        self.log.info("Chrome Webdriver initialized.")

        self.page = GooglePage(self.driver)
        self.page.open()
        self.log.info("Google page opened.")

        self.page.is_search_box_present()

    # @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_field_presence(self, setup_web):
        self.driver = setup_web
        self.driver.maximize_window()
        self.log.info("Chrome Webdriver initialized.")

        self.page = GooglePage(self.driver)
        self.page.open()
        self.log.info("Google page opened.")

        self.page.is_search_box_present()


    # @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_field_presence(self, setup_web):
        self.driver = setup_web
        self.driver.maximize_window()
        self.log.info("Chrome Webdriver initialized.")

        self.page = GooglePage(self.driver)
        self.page.open()
        self.log.info("Google page opened.")

        self.page.is_search_box_present()


    # @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_field_presence(self, setup_web):
        self.driver = setup_web
        self.driver.maximize_window()
        self.log.info("Chrome Webdriver initialized.")

        self.page = GooglePage(self.driver)
        self.page.open()
        self.log.info("Google page opened.")

        self.page.is_search_box_present()
