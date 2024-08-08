from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class PersonalDetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    myInfo_locator = "//span[text()='My Info']"
    personalDetails_locator = "//a[@class='orangehrm-tabs-item --active']"
    firstName_locator =  "//input[@name='firstName']"
    middleName_locator =  "//input[@name='middleName']"
    lastName_locator =    "//input[@name='lastName']"
    empId_locator = "(//input[@class='oxd-input oxd-input--active'])[2]"
    otherId_locator = "(//input[@class='oxd-input oxd-input--active'])[3]"
    license_number="(//input[@class='oxd-input oxd-input--active'])[4]"
    expiryDate_locator="(//input[@class='oxd-input oxd-input--active'])[5]"
    nationality_locator="(//div[@class='oxd-select-text oxd-select-text--active'])[1]"
    marital_locator="(//div[@class='oxd-select-text oxd-select-text--active'])[2]"
    dob_locator="(//input[@data-v-1f99f73c])[9]"
    male_locator=  "(//span[@data-v-7ef819fd])[1]"
    female_locator =  "(//span[@data-v-7ef819fd])[2]"
    save_locator =  "(//button[text()=' Save '])[1]"

    def personalDetails(self, Fname, Mname, Lname, Employee_id, Othr_id, Lnumber, Exp_date, dob):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.personalDetails_locator).click()

        self.find(By.XPATH, self.firstName_locator).clear()
        self.find(By.XPATH, self.middleName_locator).clear()
        self.find(By.XPATH, self.lastName_locator).clear()
        self.find(By.XPATH, self.empId_locator).clear()
        self.find(By.XPATH, self.otherId_locator).clear()
        self.find(By.XPATH, self.license_number).clear()
        self.find(By.XPATH, self.expiryDate_locator).clear()
        self.find(By.XPATH, self.dob_locator).clear()

        self.send_key(By.XPATH, self.firstName_locator, Fname)
        self.send_key(By.XPATH, self.middleName_locator, Mname)
        self.send_key(By.XPATH, self.lastName_locator, Lname)
        self.send_key(By.XPATH, self.empId_locator, str(Employee_id))
        self.send_key(By.XPATH, self.otherId_locator, str(Othr_id))
        self.send_key(By.XPATH, self.license_number, str(Lnumber))
        self.send_key(By.XPATH, self.expiryDate_locator, str(Exp_date))
        self.send_key(By.XPATH, self.dob_locator, str(dob))

    def personalDetails_mandatory(self, Fname, Mname, Lname):
        self.find(By.XPATH, self.myInfo_locator).click()
        self.find(By.XPATH, self.personalDetails_locator).click()

        self.find(By.XPATH, self.firstName_locator).clear()
        self.find(By.XPATH, self.middleName_locator).clear()
        self.find(By.XPATH, self.lastName_locator).clear()

        self.send_key(By.XPATH, self.firstName_locator, Fname)
        self.send_key(By.XPATH, self.middleName_locator, Mname)
        self.send_key(By.XPATH, self.lastName_locator, Lname)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.click(By.XPATH, self.male_locator)
        elif gender.lower() == "female":
            self.click(By.XPATH, self.female_locator)

    def select_country(self, country):
        country_dropdown = self.find(By.XPATH, self.nationality_locator)
        country_dropdown.click()
        country_option_locator = f"//span[text()='{country}']"
        country_option = self.find(By.XPATH, country_option_locator)
        country_option.click()

    def select_status(self, country):
        country_dropdown = self.find(By.XPATH, self.marital_locator)
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
