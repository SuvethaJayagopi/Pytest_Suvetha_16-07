from Pages.BasePage import BasePage
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException



class BuzzPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    buzz_locator = "//span[text()='Buzz']"
    sharePhotos_locator="//button[text()=' Share Photos']"
    addPhoto_locator="(//i[@data-v-bddebfba])[6]"
    share_locator="//button[text()=' Share ']"

    def buzz(self):
        self.find(By.XPATH, self.buzz_locator).click()
        self.find(By.XPATH, self.sharePhotos_locator).click()
        self.find(By.XPATH, self.addPhoto_locator).click()

    def share(self):
        self.find(By.XPATH, self.share_locator).click()

    def assert_saved_message_displayed(self):
        update_message_locator = (By.XPATH, "//p[text()='Successfully Saved']")
        try:
            update_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(update_message_locator))
            assert update_message.is_displayed(), "Saved message is not displayed"
            print("Saved message is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the update message.")
        except NoSuchElementException:
            print("NoSuchElementException: Saved message element not found.")


        


    