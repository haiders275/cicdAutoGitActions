import allure
from pageObjects.webApp_Page import GooglePage
from utilities.customlogger import LogGen


class TestGoogleSearchField:
    log = LogGen.loggen()

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_field_presence(self, setup_web):
        self.driver = setup_web
        self.driver.maximize_window()
        self.page = GooglePage(self.driver)
        self.page.open()
        self.page.get_title()
        self.log.info("Title is verified.")
