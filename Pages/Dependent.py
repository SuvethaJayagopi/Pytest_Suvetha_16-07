from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DependentPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    myInfo_locator = "//span[text()='My Info']"
    dependent_locator = "//a[text()='Dependents']"
    add_locator="(//button[@data-v-10d463b7])[1]"
    name_locator="(//input[@data-v-1f99f73c])[2]"
    relation_locator="//div[@data-v-67d2aedf]"
    dob_locator="(//div[@data-v-4a95a2e0])[1]"
    cancel_locator="(//button[@data-v-10d463b7])[1]"
    save_locator="(//button[@data-v-10d463b7])[2]"

    def dependent(self, name, dob):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.dependent_locator).click()
        self.find(By.XPATH, self.add_locator).click()

        self.send_key(By.XPATH, self.name_locator, name)
        self.send_key(By.XPATH, self.dob_locator, str(dob))

    def dependent_mandatory(self, name):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.dependent_locator).click()
        self.find(By.XPATH, self.add_locator).click()

        self.send_key(By.XPATH, self.name_locator, name)
      

    def select_relationship(self, relation):
        relation_dropdown = self.find(By.XPATH, self.relation_locator)
        relation_dropdown.click()
        relation_option_locator = f"//span[text()='{relation}']"
        relation_option = self.find(By.XPATH, relation_option_locator)
        relation_option.click()

    def save_details(self):
        self.click(By.XPATH, self.save_locator)

    def cancel_details(self):
        self.click(By.XPATH, self.cancel_locator)

    def assert_details_saved_successfully(self):
        update_message_locator = (By.XPATH, "//p[text()='Successfully Saved']")
        try:
            update_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(update_message_locator))
            assert update_message.is_displayed(), "saved message is not displayed"
            print("saved message is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the update message.")
        except NoSuchElementException:
            print("NoSuchElementException: Update message element not found.")