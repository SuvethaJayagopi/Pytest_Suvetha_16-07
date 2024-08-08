import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.ChangePasswordPage import ChangePasswordPage
from Utility import utility_file

current_password = "admin123"
invalidCurrentPassword = "Admin"
new_password = "User123"
invalidConfirmPassword = "user"
confirm_password = "User123"

@pytest.mark.usefixtures("setup_and_teardown")
class TestChangePassword:
    @pytest.mark.smoke
    def test_change_password(self):
        changepassword = ChangePasswordPage(self.driver)
        changepassword.valid_login() 
        changepassword.changePassword(current_password, new_password, confirm_password)
        changepassword.assert_password_change_successful()

    @pytest.mark.regression
    def test_invalid_current_password(self):
        changepassword = ChangePasswordPage(self.driver)
        changepassword.valid_login() 
        changepassword.changePassword(invalidCurrentPassword, new_password, confirm_password)
        changepassword.assert_invalid()

    @pytest.mark.smoke
    def test_invalid_confirm_password(self):
        changepassword = ChangePasswordPage(self.driver)
        changepassword.valid_login() 
        changepassword.changePassword(current_password, new_password, invalidConfirmPassword)
        changepassword.assert_alert()

    