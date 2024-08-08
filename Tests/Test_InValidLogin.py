import pytest
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Utility import ExcelReader

@pytest.mark.usefixtures("setup_and_teardown")
@pytest.mark.parametrize("username,password",ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\Invalid_LoginData.xlsx","loginInvalid"))
class TestLogin:
    @pytest.mark.smoke
    def test_invalid_login(self, username, password):
        login = LoginPage(self.driver)
        login.login(username, password)
        
        error_message = self.driver.find_element(By.XPATH, "//p[text()='Invalid credentials']")
        assert error_message.is_displayed(), "Error message for invalid login is not displayed"