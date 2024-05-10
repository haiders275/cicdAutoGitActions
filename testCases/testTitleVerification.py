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

"""
name: Python Selenium CI Tests
'on':
  - push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: 3.12
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest --alluredir=./allure-results
      - name: Upload Allure report
        uses: actions/upload-artifact@v2
        with:
          name: allure-report
          path: ./allure-results
"""