from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

class ChangePasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    user_locator = "//p[@class='oxd-userdropdown-name']"
    changePassword_locator = "(//a[@class='oxd-userdropdown-link'])[3]"
    currentPassword_locator = "(//input[@class='oxd-input oxd-input--active'])[2]"
    Password_locator = "(//input[@type='password'])[2]"
    confirmPassword_locator = "(//input[@type='password'])[3]"
    save_locator = "//button[@type='submit']"

    def changePassword(self, current_password, new_password, confirm_password):
        #self.click(By.XPATH, self.user_locator)
        self.find(By.XPATH,self.user_locator).click()
        #self.click(By.XPATH, self.changePassword_locator)
        self.find(By.XPATH,self.changePassword_locator).click()
        self.send_key(By.XPATH, self.currentPassword_locator, current_password)
        self.send_key(By.XPATH, self.Password_locator, new_password)
        #password_field = self.find(By.XPATH, self.Password_locator)        
        #password_field.send_keys(new_password)
        self.send_key(By.XPATH, self.confirmPassword_locator, confirm_password)
        self.click(By.XPATH, self.save_locator)

    def assert_password_change_successful(self):
        success_message_locator = (By.XPATH, "//p[text()='Successfully Saved']")
        success_message = self.wait.until(EC.visibility_of_element_located(success_message_locator))
        assert success_message.is_displayed(), "Change Password was not successful"

    def invalid_currentPassword(self, invalidCurrentPassword, new_password, confirm_password):
        #self.click(By.XPATH, self.user_locator)
        self.find(By.XPATH,self.user_locator).click()
        #self.click(By.XPATH, self.changePassword_locator)
        self.find(By.XPATH,self.changePassword_locator).click()
        self.send_key(By.XPATH, self.currentPassword_locator, invalidCurrentPassword)
        self.send_key(By.XPATH, self.Password_locator, new_password)
        self.send_key(By.XPATH, self.confirmPassword_locator, confirm_password)
        self.click(By.XPATH, self.save_locator)

    def assert_invalid(self):
        invalid_message_locator = (By.XPATH, "//p[text()='Current Password is Incorrect']")
        invalid_message = self.wait.until(EC.visibility_of_element_located(invalid_message_locator))
        assert invalid_message.is_displayed(), "Invalid password is not successful"

    def invalid_confirmPassword(self, invalidConfirmPassword, new_password, confirm_password):
        #self.click(By.XPATH, self.user_locator)
        self.find(By.XPATH,self.user_locator).click()
        #self.click(By.XPATH, self.changePassword_locator)
        self.find(By.XPATH,self.changePassword_locator).click()
        self.send_key(By.XPATH, self.currentPassword_locator, invalidConfirmPassword)
        self.send_key(By.XPATH, self.Password_locator, new_password)
        self.send_key(By.XPATH, self.confirmPassword_locator, confirm_password)
        self.click(By.XPATH, self.save_locator)

    def assert_alert(self):
        invalid_message_locator = (By.XPATH, "//span[text()='Passwords do not match']")
        invalid_message = self.wait.until(EC.visibility_of_element_located(invalid_message_locator))
        assert invalid_message.is_displayed(), "Invalid password is not successful"
