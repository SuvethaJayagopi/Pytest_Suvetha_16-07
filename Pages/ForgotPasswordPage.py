from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    forgotPassword_locator = "//div[@class='orangehrm-login-forgot']//p"
    username_locator = "//input[@name='username']"
    resetPassword_locator = "//button[text()=' Reset Password ']"
    cancelPassword_locator= "//button[text()=' Cancel ']"

    def forgotPassword(self, username):
        self.find(By.XPATH,self.forgotPassword_locator).click()
        self.send_key(By.XPATH, self.username_locator, username)
        self.click(By.XPATH, self.resetPassword_locator)

    def forgotPassword_cancel(self, username):
        self.find(By.XPATH,self.forgotPassword_locator).click()
        self.send_key(By.XPATH, self.username_locator, username)
        self.click(By.XPATH, self.cancelPassword_locator)
   


        
