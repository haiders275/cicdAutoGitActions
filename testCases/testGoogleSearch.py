import unittest

import allure
import pytest
from selenium import webdriver
from pageObjects.webApp_Page import GooglePage


class TestGoogleSearchField:

    @allure.severity(allure.severity_level.NORMAL)
    def test_search_field_presence(self, setup_web):
        self.driver = setup_web
        self.driver.maximize_window()
        self.page = GooglePage(self.driver)
        self.page.open()
        self.page.is_search_box_present()
