from Pages.BasePage import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



class LoginPage(BasePage):

    username_locator = "//input[@name='username']"
    password_locator = "//input[@name='password']"
    login_button_locator = "//button[@type='submit']"


    def login(self,username,password):
        self.send_key(By.XPATH,self.username_locator,str(username))
        self.send_key(By.XPATH,self.password_locator,str(password))
        self.click(By.XPATH,self.login_button_locator)
        time.sleep(5)
  
    def assert_login_successful(self):
        dashboard_element_locator = (By.XPATH, "//h6[text()='Dashboard']")
        try:
            dashboard_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(dashboard_element_locator)
            )
            assert dashboard_element.is_displayed(), "Dashboard is not displayed after login"
            print("Dashboard is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the dashboard element.")
        except NoSuchElementException:
            print("NoSuchElementException: Update message element not found.")