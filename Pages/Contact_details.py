from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ContactDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    myInfo_locator = "//span[text()='My Info']"
    contactDetails_locator = "//a[text()='Contact Details']"
    street1_locator ="(//div[@data-v-957b4417]/input)[1]"
    street2_locator ="(//input[@data-v-1f99f73c])[3]"
    city_locator ="(//div[@data-v-957b4417]/input)[3]"
    state_locator ="(//div[@data-v-957b4417]/input)[4]"
    zipCode_locator ="(//div[@data-v-957b4417]/input)[5]"
    country_locator ="//div[@class='oxd-select-text-input']"
    home_locator ="(//div[@data-v-957b4417]/input)[6]"
    mobile_locator ="(//div[@data-v-957b4417]/input)[7]"
    work_locator ="(//div[@data-v-957b4417]/input)[8]"
    workEmail_locator ="(//div[@data-v-957b4417]/input)[9]"
    otherEmail_locator ="(//div[@data-v-957b4417]/input)[10]"
    save_locator =  "(//button[text()=' Save '])[1]"

    def contactDetails(self, street1, street2, city, state, zip_code, home, mobile, work, work_email, other_email):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.contactDetails_locator).click()

        self.find(By.XPATH, self.street1_locator).clear()
        self.find(By.XPATH, self.street2_locator).clear()
        self.find(By.XPATH, self.city_locator).clear()
        self.find(By.XPATH, self.state_locator).clear()
        self.find(By.XPATH, self.zipCode_locator).clear()
        self.find(By.XPATH, self.home_locator).clear()
        self.find(By.XPATH, self.mobile_locator).clear()
        self.find(By.XPATH, self.work_locator).clear()
        self.find(By.XPATH, self.workEmail_locator).clear()
        self.find(By.XPATH, self.otherEmail_locator).clear()

        self.send_key(By.XPATH, self.street1_locator, street1)
        self.send_key(By.XPATH, self.street2_locator, street2)
        self.send_key(By.XPATH, self.city_locator, city)
        self.send_key(By.XPATH, self.state_locator, state)
        self.send_key(By.XPATH, self.zipCode_locator, str(zip_code))
        self.send_key(By.XPATH, self.home_locator, str(home))
        self.send_key(By.XPATH, self.mobile_locator, str(mobile))
        self.send_key(By.XPATH, self.work_locator, str(work))
        self.send_key(By.XPATH, self.workEmail_locator, work_email)
        self.send_key(By.XPATH, self.otherEmail_locator, other_email)

    def select_country(self, country):
        country_dropdown = self.find(By.XPATH, self.country_locator)
        country_dropdown.click()
        country_option_locator = f"//span[text()='{country}']"
        country_option = self.find(By.XPATH, country_option_locator)
        country_option.click()

    def save_details(self):
        self.click(By.XPATH, self.save_locator)


    def assert_details_saved_successfully(self):
        update_message_locator = (By.XPATH, "//p[text()='Successfully Updated']")
        try:
            update_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(update_message_locator))
            assert update_message.is_displayed(), "Update message is not displayed"
            print("Update message is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the update message.")
        except NoSuchElementException:
            print("NoSuchElementException: Update message element not found.")

    def assert_same_email_error_displayed(self):
        error_message_locator = (By.XPATH, "//span[text()='Work Email and Other Email cannot be the same']")
        try:
            error_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(error_message_locator))
            assert error_message.is_displayed(), "Error message is not displayed"
            print("Error message is displayed successfully.")
        except TimeoutException:
            print("TimeoutException occurred while waiting for the error message.")
        except NoSuchElementException:
            print("NoSuchElementException: Update message element not found.")




