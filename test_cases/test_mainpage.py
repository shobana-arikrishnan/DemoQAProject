import pytest as pytest

from scenarios.main_page import DemoQAMainPage
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class TestMainPage:

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.quit()

    @pytest.fixture
    def startup_page(self,driver):
        yield DemoQAMainPage(self.driver)

    @pytest.fixture
    def setup_page(self,startup_page):
        startup_page.browsepage()
        yield startup_page

    def test_title(self,setup_page):
        assert setup_page.check_title()

    def test_check_menu_availability(self,setup_page):
        assert setup_page.check_menu_availability()
        