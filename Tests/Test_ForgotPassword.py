import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.ForgotPasswordPage import ForgotPasswordPage
from Utility import utility_file

@pytest.mark.usefixtures("setup_and_teardown")
class TestForgotPassword:
    @pytest.mark.smoke
    def test_forgot_password(self):
        forgotpassword=ForgotPasswordPage(self.driver)
        username = utility_file.get_config("valid login details", "username")

        forgotpassword.forgotPassword(username)

        success_message_locator = (By.XPATH, "//div[@class='orangehrm-card-container']//h6")
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(success_message_locator)
        )
        assert success_message.is_displayed(), "Forgot password process was not successful"

    @pytest.mark.regression
    def test_forgot_password_cancel(self):
        forgotpassword = ForgotPasswordPage(self.driver)
        username = utility_file.get_config("valid login details", "username")
        
        forgotpassword.forgotPassword_cancel(username)
        
        loginPage_locator = (By.XPATH, "//h5[text()='Login']")
        login = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loginPage_locator)
        )
        assert login.is_displayed(), "Cancel was not successful"