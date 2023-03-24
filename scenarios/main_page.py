from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from locators.locators import DemoQALocators
from data.data import DemoQAData

class DemoQAMainPage:
    def __init__(self,driver):
        self.url = DemoQAData().url
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    def browsepage(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self
    
    def check_title(self):
        verify_title = self.driver.title == DemoQAData().title
        return verify_title

    def check_menu_availability(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH,DemoQALocators().elements_menu_locator)))
            self.wait.until(EC.presence_of_element_located((By.XPATH,DemoQALocators().forms_menu_locator)))
            self.wait.until(EC.presence_of_element_located((By.XPATH,DemoQALocators().alert_frame_windows_menu_locator)))
            self.wait.until(EC.presence_of_element_located((By.XPATH,DemoQALocators().widgets_menu_locator)))
            self.wait.until(EC.presence_of_element_located((By.XPATH,DemoQALocators().interactions_menu_locator)))
            self.wait.until(EC.presence_of_element_located((By.XPATH,DemoQALocators().book_store_application_menu_locator)))
            return True
        except NoSuchElementException:
            return False
                        