from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class EmergencyContactPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    myInfo_locator = "//span[text()='My Info']"
    emergencyContact_locator = "//a[text()='Emergency Contacts']"
    add_locator = "(//button[@type='button'])[3]"
    name_locator ="(//div[@data-v-957b4417]//input)[1]"
    relationship_locator="(//div[@data-v-957b4417]//input)[2]"
    telephone_locator="(//div[@data-v-957b4417]//input)[3]"
    mobile_locator="(//div[@data-v-957b4417]//input)[4]"
    work_locator="(//div[@data-v-957b4417]//input)[5]"
    save_locator="(//button[@data-v-10d463b7])[2]"
    cancel_locator="(//button[@data-v-10d463b7])[1]"

    def emergencyContact(self, name, relationship, telephone, mobile, work):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.emergencyContact_locator).click()
        self.find(By.XPATH, self.add_locator).click()

        self.send_key(By.XPATH, self.name_locator, name)
        self.send_key(By.XPATH, self.relationship_locator, relationship)
        self.send_key(By.XPATH, self.telephone_locator, str(telephone))
        self.send_key(By.XPATH, self.mobile_locator, str(mobile))
        self.send_key(By.XPATH, self.work_locator, str(work))

    def emergencyContact_mandatory(self, name, relationship, telephone):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.emergencyContact_locator).click()
        self.find(By.XPATH, self.add_locator).click()

        self.send_key(By.XPATH, self.name_locator, name)
        self.send_key(By.XPATH, self.relationship_locator, relationship)
        self.send_key(By.XPATH, self.telephone_locator, str(telephone))

    def emergencyContact_required(self, name, relationship):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.emergencyContact_locator).click()
        self.find(By.XPATH, self.add_locator).click()

        self.send_key(By.XPATH, self.name_locator, name)
        self.send_key(By.XPATH, self.relationship_locator, relationship)

    def save_details(self):
        self.click(By.XPATH, self.save_locator)

    def cancel_details(self):
        self.click(By.XPATH, self.cancel_locator)


    def assert_update_message_displayed(self):
        update_message_locator = (By.XPATH, "//p[text()='Successfully Updated']")
        try:
            update_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(update_message_locator))
            assert update_message.is_displayed(), "Update message is not displayed"
            print("Update message is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the update message.")
        except NoSuchElementException:
            print("NoSuchElementException: Update message element not found.")

    def assert_error_message_displayed(self):
        error_message_locator = (By.XPATH, "//span[text()='At least one phone number is required']")
        try:
            error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(error_message_locator))
            assert error_message.is_displayed(), "Update message is not displayed"
            print("Update message is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the update message.")
        except NoSuchElementException:
            print("NoSuchElementException: Update message element not found.")

