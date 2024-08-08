from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class ImmigrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    myInfo_locator = "//span[text()='My Info']"
    immigration_locator = "//a[text()='Immigration']"
    add_locator="(//button[@data-v-10d463b7])[1]"
    passport_locator = "(//span[@data-v-7ef819fd])[1]"
    visa_locator = "(//span[@data-v-7ef819fd])[2]"
    number_locator="(//input[@data-v-1f99f73c])[2]"
    issuedDate_locator="(//input[@data-v-1f99f73c])[3]"
    expiryDate_locator="(//input[@data-v-1f99f73c])[4]"
    status_locator="(//input[@data-v-1f99f73c])[5]"
    issuedBy_locator="//div[@data-v-67d2aedf]"
    reviewDate_locator="(//input[@data-v-1f99f73c])[6]"
    comment_locator="//textarea[@data-v-bd337f32]"
    save_locator="(//button[@data-v-10d463b7])[2]"
    cancel_locator="(//button[@data-v-10d463b7])[1]"

    def add_immigration_details(self, number, issued_date, expiry_date, status, review_date, comment):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.immigration_locator).click()
        self.find(By.XPATH, self.add_locator).click()
        self.find(By.XPATH, self.passport_locator).click()

        self.send_key(By.XPATH, self.number_locator, str(number))
        self.send_key(By.XPATH, self.issuedDate_locator, str(issued_date))
        self.send_key(By.XPATH, self.expiryDate_locator, str(expiry_date))
        self.send_key(By.XPATH, self.status_locator, status)
        self.send_key(By.XPATH, self.reviewDate_locator, str(review_date))
        self.send_key(By.XPATH, self.comment_locator, comment)

    def select_country(self, country):
        country_dropdown = self.find(By.XPATH, self.issuedBy_locator)
        country_dropdown.click()
        country_option_locator = f"//span[text()='{country}']"
        country_option = self.find(By.XPATH, country_option_locator)
        country_option.click()

    def save_details(self):
        self.click(By.XPATH, self.save_locator)

    def cancel_details(self):
        self.click(By.XPATH, self.cancel_locator)

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
        