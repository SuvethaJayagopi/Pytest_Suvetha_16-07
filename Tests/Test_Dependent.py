import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Dependent import DependentPage
from Utility import ExcelReader

@pytest.mark.usefixtures("setup_and_teardown")
class TestDependent:
    @pytest.mark.smoke
    @pytest.mark.parametrize("name,dob", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\DependentData.xlsx", "dependent"))
    def test_add_dependent(self, name, dob):  
        dependent_page = DependentPage(self.driver)  
        dependent_page.valid_login()  
        dependent_page.dependent(name, dob)  
        dependent_page.select_relationship("Child")
        dependent_page.save_details()  
        dependent_page.assert_details_saved_successfully()

    @pytest.mark.regression
    @pytest.mark.parametrize("name,dob", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\DependentData.xlsx", "dependent"))
    def test_add_dependent_cancel(self, name, dob):  
        dependent_page = DependentPage(self.driver)  
        dependent_page.valid_login()  
        dependent_page.dependent(name, dob)  
        dependent_page.select_relationship("Child")
        dependent_page.cancel_details()  

    @pytest.mark.parametrize("name", ["Suvetha"])
    def test_add_dependent_mandatory(self, name):  
        dependent_page = DependentPage(self.driver)  
        dependent_page.valid_login()  
        dependent_page.dependent_mandatory(name)  
        dependent_page.select_relationship("Child")
        dependent_page.save_details()  
        dependent_page.assert_details_saved_successfully()

