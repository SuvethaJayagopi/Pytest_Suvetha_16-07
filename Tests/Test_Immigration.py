import pytest
from Pages.Immigration import ImmigrationPage
from Utility import ExcelReader

@pytest.mark.usefixtures("setup_and_teardown")
class TestImmigration:

    @pytest.mark.smoke
    @pytest.mark.parametrize("number, issued_date, expiry_date, status, review_date, comment", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\ImmigrationData.xlsx", "immigration"))
    def test_add_immigration_details(self, number, issued_date, expiry_date, status, review_date, comment):  
        immigration_page = ImmigrationPage(self.driver)  
        immigration_page.valid_login()  
        immigration_page.add_immigration_details(number, issued_date, expiry_date, status, review_date, comment)  
        immigration_page.select_country("Algeria")
        immigration_page.save_details()  
        immigration_page.assert_details_saved_successfully()

    @pytest.mark.regression
    @pytest.mark.parametrize("number, issued_date, expiry_date, status, review_date, comment", ExcelReader.get_data("C:\\Users\\SM\\Desktop\\Suvetha_pytest(8-6)\\Pytest_OrangeHRM\\Excel_Files\\ImmigrationData.xlsx", "immigration"))
    def test_add_immigration_details_cancel(self, number, issued_date, expiry_date, status, review_date, comment):  
        immigration_page = ImmigrationPage(self.driver)  
        immigration_page.valid_login()  
        immigration_page.add_immigration_details(number, issued_date, expiry_date, status, review_date, comment)  
        immigration_page.select_country("Algeria")
        immigration_page.cancel_details()  
